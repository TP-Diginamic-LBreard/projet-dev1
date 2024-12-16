from src.repositories.objet_repository import get_all_objects, get_object, delete, create, update


def get_all(db): 
    return get_all_objects(db)

def get_object_byId(id, db): 
    return get_object(id, db)

def create_object(object, db):
    return create(object, db)

def update_object(object, db):
    return update(object, db)

def delete_object_byId(id, db): 
    return delete(id, db)