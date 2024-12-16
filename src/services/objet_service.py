from src.repositories.objet_repository import get_all_objects, get_object

def get_all(db): 
    return get_all_objects(db)

def get_object_byID(db): 
    return get_object(db)