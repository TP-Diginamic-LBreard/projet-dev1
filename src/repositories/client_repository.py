from src.models import Client

# Récupérer tous les clients
def get_all_clients(db):
    return db.query(Client).all()

# Créer un nouveau client
def create_client(db, client_data: dict):
    new_client = Client(**client_data)
    db.add(new_client)
    db.commit()
    db.refresh(new_client)
    return new_client

# Récupérer un client par ID
def get_client_by_id(db, id):
    client = db.query(Client).filter(Client.codcli == id).first()
    if not client:
        raise ValueError(f"Client avec l'ID {id} introuvable.")
    return client

# Mettre à jour un client
def update_client(db, id, client_data: dict):
    client = get_client_by_id(db, id)
    if client:
        for key, value in client_data.items():
            setattr(client, key, value)
        db.commit()
        db.refresh(client)
    return client

# Supprimer un client
def delete_client(db, id):
    client = get_client_by_id(db, id)
    if client:
        db.delete(client)
        db.commit()
    return client

