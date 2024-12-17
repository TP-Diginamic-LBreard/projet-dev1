from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.services.client_service import (
    get_all_clients_service,
    get_client_by_id_service,
    create_client_service,
    update_client_service,
    delete_client_service,
)
from src.database import get_db
from src.models import Client

router = APIRouter()

# Route GET pour lire tous les clients
@router.get("/clients", response_model=list[Client])
def read_all_clients(db: Session = Depends(get_db)):
    clients = get_all_clients_service(db)
    return clients

# Route GET pour lire un client par ID
@router.get("/clients/{id}", response_model=Client)
def read_client(id: int, db: Session = Depends(get_db)):
    client = get_client_by_id_service(db, id)
    if not client:
        raise HTTPException(status_code=404, detail="Client non trouvé")
    return client

# Route POST pour créer un nouveau client
@router.post("/clients", response_model=Client)
def create_client(client: Client, db: Session = Depends(get_db)):
    return create_client_service(db, client)

# Route PUT pour mettre à jour un client par ID
@router.put("/clients/{id}", response_model=Client)
def update_client(id: int, client: Client, db: Session = Depends(get_db)):
    updated_client = update_client_service(db, id, client)
    if not updated_client:
        raise HTTPException(status_code=404, detail="Client non trouvé")
    return updated_client

# Route DELETE pour supprimer un client par ID
@router.delete("/clients/{id}")
def delete_client(id: int, db: Session = Depends(get_db)):
    success = delete_client_service(db, id)
    if not success:
        raise HTTPException(status_code=404, detail="Client non trouvé")
    return {"message": "Client supprimé avec succès"}




