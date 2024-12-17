from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from src.database import get_db
from src.models import Client
<<<<<<< Updated upstream
from src.services.client_service import get_all, create_client_db
=======
from src.services.client_service import (
    get_all, create_new_client, get_client, update_existing_client, delete_existing_client
)
>>>>>>> Stashed changes

router_client = APIRouter(prefix="/client", tags=["client"])

@router_client.get("/")
def read_clients(db: Session = Depends(get_db)):
    return get_all(db)

@router_client.get("/{id}")
def read_client_by_id(id: int, db: Session = Depends(get_db)):
    try:
        client = get_client(db, id)
        if not client:
            raise HTTPException(status_code=404, detail="Client non trouvé.")
        return client
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

<<<<<<< Updated upstream
@router_client.post("/{id}")
def create_client_db ((client: Client, db: Session = Depends(get_db)):)
    try:
        return create_client(db, client)
=======
@router_client.post("/")
def create_client(client: dict, db: Session = Depends(get_db)):
    try:
        return create_new_client(db, client)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router_client.put("/{id}")
def update_client(id: int, client_data: dict, db: Session = Depends(get_db)):
    try:
        return update_existing_client(db, id, client_data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router_client.delete("/{id}")
def delete_client(id: int, db: Session = Depends(get_db)):
    try:
        success = delete_existing_client(db, id)
        if success:
            return {"message": "Utilisateur supprimé"}
        else:
            raise HTTPException(status_code=404, detail="Client non trouvé")
>>>>>>> Stashed changes
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
