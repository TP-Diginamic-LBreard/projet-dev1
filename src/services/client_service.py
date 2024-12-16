from src.repositories.client_repository import get_all_clients, create_client, get_client_by_id

# Récupérer tous les clients

def get_all(db): 
    return get_all_clients(db)

# Créer un nouveau client

def create_client(db, client_data):
    if not client_data.name
        raise ValueError("Le nom et l'email sont obligatoires pour créer un client.")
    return create_client_db (db, client_data)
