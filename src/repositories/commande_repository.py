from sqlalchemy import select, insert
from sqlalchemy.orm import Session

from src.models import Commande


def get_commandes(db):
    return db.scalars(select(Commande)).all()


def get_commande(id: int, db: Session) -> Commande:
    return db.get(Commande, id)


def add_commande(commande: Commande, db: Session) -> int:
    db.add(commande)
    db.flush()
    db.refresh(commande)
    return commande.codcde


def update_commande(id: int, commande: Commande, db: Session):
    pass


def delete_commande(commande: Commande, db: Session):
    db.delete(commande)
