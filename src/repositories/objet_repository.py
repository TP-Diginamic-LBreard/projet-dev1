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
    new_object = Objet(**object.model_dump())
    # add optionnal attributes that have been defined
    db.add(new_object)
    db.commit()
    db.refresh(new_object)
    return new_object

def update(ObjectUpdate: ObjectUpdate, object: Objet, db):
    update_data = ObjectUpdate.model_dump(exclude_unset=True)  # transform schema in dictionnary and exclude undifined values
    for key, value in update_data.items():
        setattr(object, key, value) # update attributes with defined values
    db.add(object)
    db.commit()
    db.refresh(object)
    return object

def delete(id: int, db):
    # delete targeted object
    db.query(Objet).filter(Objet.codobj == id).delete()
    db.commit()
    return


