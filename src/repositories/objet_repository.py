from src.models import Objet
from src.schemas.object_schema import ObjectSchema

def get_all_objects(db):
    # get list of all objets
    return list(db.query(Objet).all())

def get_object(id: int, db):
    return db.query(Objet).get(id)

def create(object: ObjectSchema, db):
    new_object = Objet(
        codobj=object.codobj,
        libobj=object.libobj,
        tailleobj= object.tailleobj,
        poidsobj= object.poidsobj,
        points= object.points)

    db.add(new_object)
    db.commit()
    return

def update(id: int, new_libobj: str, db):
    print(id)
    query = db.query(Objet).filter(Objet.codobj == id).first()
    query.libobj = new_libobj
    db.add(query)
    db.commit()
    return

def delete(id: int, db):
    test = db.query(Objet).filter(Objet.codobj == id).delete()
    db.commit()
    return test


