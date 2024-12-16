from src.models import Client

def get_all_clients(db):
    # get all clients
    return list(db.query(Client).all())