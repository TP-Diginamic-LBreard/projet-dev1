from src.repositories.conditionnement_repository import get_all_conditionnement, get_conditionnement, delete, create, update
from src.repositories.objet_repository import get_object

# service connect the endpoints to the right repository function
def get_all(db): 
    return get_all_conditionnement(db)

def get_conditionnement_byId(id, db): 
    return get_conditionnement(id, db)

def create_conditionnement(conditionnement, db):
    if get_object(conditionnement.codobj, db): # check that object exist to avoid IntegrityError
        return create(conditionnement, db)
    else:
        raise Exception("objet inconnu")

def update_conditionnement(id, conditionnementUpdate, db):
    conditionnement = get_conditionnement_byId(id, db)
    print(conditionnement)
    if not conditionnement : # check that conditionnement and object exist to avoid IntegrityError
        raise Exception("conditionnement inconnu")
    elif not get_object(conditionnementUpdate.codobj, db):
        raise Exception("objet inconnu")
    else:
        return update(conditionnementUpdate, conditionnement, db)

def delete_conditionnement_byId(id, db): 
    return delete(id, db)