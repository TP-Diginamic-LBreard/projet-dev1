from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from src.database import get_db
from src.models import Client
from src.services.client_service import get_all


# le tag permet d'organiser les endpoint dans la doc
router_client = APIRouter(prefix="/client", tags=["client"])

@router_client.get("/")
def get_client(db: Session = Depends(get_db)):
    try:
        return get_all(db)
    except:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@router_client.get("/{id}")
def read_client(id: int, db: Session = Depends(get_db)):
    return db.query(Client).get(id)



