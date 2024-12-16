from src.models import Objet

def get_all_objects(db):
    # get list of all objets
    return list(db.query(Objet).all())

def get_object(id: int, db):
    return db.query(Objet).get(id)