from src.repositories.conditionnement_repository import get_all_conditionnement, get_conditionnement, delete, create, update

# service connect the endpoints to the right repository function
def get_all(db): 
    return get_all_conditionnement(db)

def get_conditionnement_byId(id, db): 
    return get_conditionnement(id, db)

def create_conditionnement(conditionnement, db):
    return create(conditionnement, db)

def update_conditionnement(id, conditionnement, db):
    return update(id, conditionnement, db)

def delete_conditionnement_byId(id, db): 
    return delete(id, db)