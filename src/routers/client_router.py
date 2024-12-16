from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from src.database import get_db
from src.models import Client
from src.services.client_service import get_all, create_client_db


# le tag permet d'organiser les endpoint dans la doc
router_client = APIRouter(prefix="/client", tags=["client"])

@router_client.get("/")
def read_client(db = Depends(get_db)):
    try:
        return get_all(db)
    except:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@router_client.get("/{id}")
def read_client(id: int, db: Session = Depends(get_db)):
    return db.query(Client).get(id)

@router_client.post("/{id}")
def create_client_db ((client: Client, db: Session = Depends(get_db)):)
    try:
        return create_client(db, client)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
