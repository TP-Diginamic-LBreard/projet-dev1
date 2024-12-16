from src.models import Objet
from src.schemas.object_schema import ObjectUpdate, ObjectCreate

def get_all_objects(db):
    # get list of all objets
    return list(db.query(Objet).all())

def get_object(id: int, db):
    #  get object by id
    return db.query(Objet).get(id)

def create(object: ObjectCreate, db):
    # create new object with mandatory data from the schema
    new_object = Objet(
        codobj=object.codobj,
        libobj=object.libobj,
        tailleobj= object.tailleobj,
        poidsobj= object.poidsobj,
        points= object.points)
    # add optionnal attributes that have been defined
    new_data = object.model_dump(exclude_unset=True)  # transform schema in dictionnary and exclude undifined values
    for key, value in new_data.items():
        setattr(new_object, key, value) # add attributes with defined values
    db.add(new_object)
    db.commit()
    return

def update(ObjectUpdate: ObjectUpdate, db):
    query = db.query(Objet).get(ObjectUpdate.codobj) # get the targeted object
    update_data = ObjectUpdate.model_dump(exclude_unset=True)  # transform schema in dictionnary and exclude undifined values
    for key, value in update_data.items():
        setattr(query, key, value) # update attributes with defined values
    db.add(query)
    db.commit()
    return

def delete(id: int, db):
    # delete targeted object
    test = db.query(Objet).filter(Objet.codobj == id).delete()
    db.commit()
    return test


