from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from src.database import get_db
from src.services.conditionnement_service import get_all_conditionnement, get_conditionnement_byId, delete_conditionnement_byId, create_conditionnement, update_conditionnement
from src.schemas.conditionnement_schema import ConditionnementCreate, ConditionnementUpdate


# le tag permet d'organiser les endpoint dans la doc
router_conditionnement = APIRouter(prefix="/conditionnement", tags=["conditionnement"])

@router_conditionnement.get("/")
def get_oconditionnement(db = Depends(get_db)):
    try:
        return get_all_conditionnement(db)
    except:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@router_conditionnement.get("/{id}")
def get_conditionnement(id: int, db: Session = Depends(get_db)):
    try:
        return get_conditionnement_byId(id, db)
    except:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@router_conditionnement.post("/create")
def post_conditionnement(conditionnement: ConditionnementCreate ,db = Depends(get_db)):
    try:
        return create_conditionnement(conditionnement, db)
    except:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR)


@router_conditionnement.put("/update/{id}")
def put_conditionnement(conditionnement: ConditionnementUpdate, db = Depends(get_db)):
    try:
        return update_conditionnement(conditionnement, db)
    except: 
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR)

@router_conditionnement.delete("/{id}/delete")
def delete_conditionnement(id: int, db = Depends(get_db)):
    try:
        return delete_conditionnement_byId(id, db)
    except:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR)



