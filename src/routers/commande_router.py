from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, Response, status
from fastapi.responses import PlainTextResponse
from sqlalchemy.orm import Session

from src.database import get_db
from src.schemas import PartialCommande, Commande, FullCommande
import src.services.commande_service as service


router_commande = APIRouter(prefix="/commande", tags=["commande"])


@router_commande.get(
        "/",
        summary="Liste des commandes"
)
def get_commandes(db = Depends(get_db)) -> list[FullCommande]:
    try:
        return service.get_commandes(db)
    except Exception as e:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@router_commande.post(
        "/",
        summary="Nouvelle commande",
        status_code=status.HTTP_201_CREATED,
        response_class=PlainTextResponse,
)
def post_commande(
        commande: Commande,
        db = Depends(get_db)
) -> str:
    try:
        id = service.add_commande(commande, db)
    except Exception as e:
        # Failure ⇒ rollback
        db.rollback()
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    else:
        # Success ⇒ commit and return (avoid finally)
        db.commit()
        return f"/commande/{id}"


@router_commande.put(
        "/",
        status_code=status.HTTP_201_CREATED,
        response_class=PlainTextResponse,
        responses={
            201: {"description": "Commande crée"},
            204: {"description": "Commande modifiée"},
        },
)
def put_commande(
        commande: FullCommande,
        response: Response,
        db = Depends(get_db)
) -> Optional[str]:
    try:
        id = service.put_commande(commande, db)
    except Exception as e:
        # Failure ⇒ rollback
        db.rollback()
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    else:
        # Success ⇒ commit and return (avoid finally)
        db.commit()
        if id:
            return f"/commande/{id}"
        else:
            response.status_code = status.HTTP_204_NO_CONTENT
            return None


@router_commande.get(
        "/{id}",
        summary="Détails d'une commande",
        responses={
            404: {},
        },
)
def get_commande(
        id: int,
        db: Session = Depends(get_db)
) -> FullCommande:
    try:
        return service.get_commande(id, db)
    except ValueError:
        # Unknown ID
        raise HTTPException(status.HTTP_404_NOT_FOUND)
    except Exception as e:
        # Other error
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@router_commande.patch(
        "/{id}",
        summary="Modification d'une commande",
        status_code=status.HTTP_204_NO_CONTENT,
        responses={
            404: {},
        },
)
def patch_commande(
        id: int,
        commande: PartialCommande,
        db: Session = Depends(get_db)
):
    try:
        service.update_commande(id, commande, db)
    except ValueError:
        # Unknown ID
        # Failure ⇒ rollback
        db.rollback()
        raise HTTPException(status.HTTP_404_NOT_FOUND)
    except Exception as e:
        # Other error
        # Failure ⇒ rollback
        db.rollback()
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    else:
        # Success ⇒ commit and return (avoid finally)
        db.commit()


@router_commande.delete(
        "/{id}",
        summary="Suppression d'une commande",
        status_code=status.HTTP_204_NO_CONTENT,
        responses={
            404: {},
        },
)
def delete_commande(
        id: int,
        db: Session = Depends(get_db)
):
    try:
        service.delete_commande(id, db)
    except ValueError:
        # Unknown ID
        # Failure ⇒ rollback
        db.rollback()
        raise HTTPException(status.HTTP_404_NOT_FOUND)
    except Exception as e:
        # Other error
        # Failure ⇒ rollback
        db.rollback()
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    else:
        # Success ⇒ commit and return (avoid finally)
        db.commit()
