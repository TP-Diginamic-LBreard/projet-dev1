from src.models import Conditionnement
from src.schemas.conditionnement_schema import ConditionnementUpdate, ConditionnementCreate

def get_all_conditionnement(db):
    # get list of all conditionnement
    return list(db.query(Conditionnement).all())

def get_conditionnement(id: int, db):
    #  get conditionnement by id
    return db.query(Conditionnement).get(id)

def create(conditionnement: ConditionnementCreate, db):
    # create new conditionnement with mandatory data from the schema
    new_conditionnement = Conditionnement(conditionnement.model_dump())
    db.add(new_conditionnement)
    db.commit()
    db.refresh(new_conditionnement)
    return new_conditionnement

# Set the id in the path
def update(conditionnementUpdate: ConditionnementUpdate, db):
    query = db.query(Conditionnement).get(conditionnementUpdate.codobj) # get the targeted conditionnement
    update_data = conditionnementUpdate.model_dump(exclude_unset=True)  # transform schema in dictionnary and exclude undifined values
    for key, value in update_data.items():
        setattr(query, key, value) # update attributes with defined values
    db.add(query)
    db.commit()
    return

def delete(id: int, db):
    # delete targeted conditionnement
    test = db.query(Conditionnement).filter(Conditionnement.codobj == id).delete()
    db.commit()
    return test


