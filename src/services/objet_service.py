from src.repositories.objet_repository import get_all_objects, get_object, delete, create, update


def get_all(db): 
    return get_all_objects(db)

def get_object_byId(id, db): 
    return get_object(id, db)

# def create_object(new_codobj: int, new_libobj: str, db):
#     return create(new_codobj, new_libobj, db)

def create_object(objet, db):
    return create(objet, db)

def update_object(id, new_libobj, db):
    return update(id, new_libobj, db)

def delete_object_byId(id, db): 
    return delete(id, db)