from typing import Optional
from sqlalchemy.orm import Session

import src.repositories.commande_repository as repository
from src.schemas import PartialCommande, Commande, FullCommande


def get_commandes(db: Session) -> [FullCommande]:
    commandes = repository.get_commandes(db)
    return list(map(lambda c: FullCommande.from_model(c), commandes))


def get_commande(id: int, db: Session) -> FullCommande:
    commande = repository.get_commande(id, db)
    if commande:
        return FullCommande.from_model(commande)
    else:
        raise ValueError('Commande inconnue')


def add_commande(commande: Commande, db: Session) -> int:
    return repository.add_commande(commande.to_model(), db)


def put_commande(commande: Commande, db: Session) -> Optional[int]:
    try:
        update_commande(commande.id, commande, db)
    except ValueError:
        return add_commande(commande, db)


def update_commande(id: int, partial_commande: PartialCommande, db: Session):
    commande = repository.get_commande(id, db)
    if commande:
        partial_commande.merge_model(commande)
    else:
        raise ValueError('Commande inconnue')


def delete_commande(id: int, db: Session):
    commande = repository.get_commande(id, db)
    if commande:
        repository.delete_commande(commande, db)
    else:
        raise ValueError('Commande inconnue')
