from src.models import Client
from sqlalchemy.orm import Session


def get_all_clients(db):
    # get all clients
    return list(db.query(Client).all())


def get_client_by_id(db: Session, client_id: int):
    # Récupère un client par son ID.
    return db.query(Client).filter(Client.codcli == client_id).first()


def create_client(db: Session, client_data: dict):
    # Crée un nouveau client avec les données fournies.
    new_client = Client(**client_data)  # Décompresse le dictionnaire pour remplir les champs
    db.add(new_client)
    db.commit()
    db.refresh(new_client)
    return new_client


def update_client(db: Session, client_id: int, client_data: dict):
    # Met à jour les informations d'un client existant.
    client = db.query(Client).filter(Client.codcli == client_id).first()
    if client:
        for key, value in client_data.items():
            setattr(client, key, value)  # Met à jour chaque champ avec les nouvelles valeurs
        db.commit()
        db.refresh(client)
    return client


def delete_client(db: Session, client_id: int):
    # Supprime un client par son ID.
    client = db.query(Client).filter(Client.codcli == client_id).first()
    if client:
        db.delete(client)
        db.commit()
        return True
    return False
