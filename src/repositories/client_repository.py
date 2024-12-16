from src.models import Client

# Récupérer tous les clients
def get_all_clients(db):

    return list(db.query(Client).all())

# Créer un nouveau client
def create_client(db, client_data):
    new_client = Client(**client_data.dict())  # Convertit les données en objet Client
    db.add(new_client)
    db.commit()
    db.refresh(new_client)  # Recharge l'objet avec ses données dans la base
    return new_client
    
# Récupérer un client par ID
def get_client_by_id(db, id):
    return db.query(Client).filter(id)