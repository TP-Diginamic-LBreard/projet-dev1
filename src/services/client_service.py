from src.repositories.client_repository import (
    get_all_clients, create_client, get_client_by_id, update_client, delete_client
)

# Récupérer tous les clients
def get_all(db):
    return get_all_clients(db)

# Créer un nouveau client
def create_new_client(db, client_data: dict):
    if not client_data.get("nomcli"):
        raise ValueError("Le nom est obligatoires pour créer un client.")
    return create_client(db, client_data)

# Récupérer un client par ID
def get_client(db, client_id):
    return get_client_by_id(db, client_id)

# Mettre à jour un client existant
def update_existing_client(db, client_id, client_data: dict):
    client = update_client(db, client_id, client_data)
    if not client:
        raise ValueError("Client non trouvé ou impossible à mettre à jour.")
    return client

# Supprimer un client
def delete_existing_client(db, client_id):
    client = delete_client(db, client_id)
    if not client:
        raise ValueError("Client non trouvé ou déjà supprimé.")
    return client
