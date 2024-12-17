from sqlalchemy.orm import Session
from src.repositories.client_repository import (
    get_all_clients as repo_get_all_clients,
    get_client_by_id as repo_get_client_by_id,
    create_client as repo_create_client,
    update_client as repo_update_client,
    delete_client as repo_delete_client
)

def get_all_clients_service(db: Session):
    # Service pour récupérer tous les clients.
    return repo_get_all_clients(db)

def get_client_by_id_service(db: Session, client_id: int):
    # Service pour récupérer un client par son ID.
    client = repo_get_client_by_id(db, client_id)
    if not client:
        return {"error": "Client non trouvé"}
    return client

def create_client_service(db: Session, client_data: dict):
    # Service pour créer un nouveau client.
    return repo_create_client(db, client_data)

def update_client_service(db: Session, client_id: int, client_data: dict):
    # Service pour mettre à jour un client.
    client = repo_update_client(db, client_id, client_data)
    if not client:
        return {"error": "Client non trouvé ou mise à jour impossible"}
    return client

def delete_client_service(db: Session, client_id: int):
    # Service pour supprimer un client.
    success = repo_delete_client(db, client_id)
    if not success:
        return {"error": "Client non trouvé ou suppression impossible"}
    return {"message": "Client supprimé avec succès"}
