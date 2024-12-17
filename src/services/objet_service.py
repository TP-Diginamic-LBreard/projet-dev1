from src.repositories.objet_repository import get_all_objects, get_object, delete, create, update

# service connect the endpoints to the right repository function
def get_all(db): 
    return get_all_objects(db)

def get_object_byId(id, db): 
    return get_object(id, db)

def create_object(object, db):
    return create(object, db)

def update_object(id, object, db):
    return update(id, object, db)

def delete_object_byId(id, db): 
    return delete(id, db)