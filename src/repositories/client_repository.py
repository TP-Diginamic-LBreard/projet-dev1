from src.models import Client
from sqlalchemy.orm import Session

def get_all_clients(db: Session):
    # get all clients
    return list(db.query(Client).all())