from src.models import Conditionnement
from src.schemas.conditionnement_schema import ConditionnementUpdate, ConditionnementCreate

def get_all_conditionnement(db):
    # get list of all objets
    return list(db.query(Conditionnement).all())

def get_conditionnement(id: int, db):
    #  get object by id
    return db.query(Conditionnement).get(id)

def create(conditionnement: ConditionnementCreate, db):
    # create new object with mandatory data from the schema
    new_conditionnement = Conditionnement(
        idcondit=conditionnement.idcondit,
        libcondit=conditionnement.libcondit,
        poidscondit= conditionnement.poidscondit,
        prixcond= conditionnement.prixcond,
        ordreimp= conditionnement.ordreimp)
    # add optionnal attributes that have been defined
    new_data = conditionnement.model_dump(exclude_unset=True)  # transform schema in dictionnary and exclude undifined values
    for key, value in new_data.items():
        setattr(new_conditionnement, key, value) # add attributes with defined values
    db.add(new_conditionnement)
    db.commit()
    return

def update(conditionnementUpdate: ConditionnementUpdate, db):
    query = db.query(Conditionnement).get(conditionnementUpdate.codobj) # get the targeted object
    update_data = conditionnementUpdate.model_dump(exclude_unset=True)  # transform schema in dictionnary and exclude undifined values
    for key, value in update_data.items():
        setattr(query, key, value) # update attributes with defined values
    db.add(query)
    db.commit()
    return

def delete(id: int, db):
    # delete targeted object
    test = db.query(Conditionnement).filter(Conditionnement.codobj == id).delete()
    db.commit()
    return test


