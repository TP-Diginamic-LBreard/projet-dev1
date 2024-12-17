from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from src.database import get_db
from src.services.objet_service import get_all, get_object_byId, delete_object_byId, create_object, update_object
from src.schemas.object_schema import ObjectCreate, ObjectUpdate


# le tag permet d'organiser les endpoint dans la doc
router_object = APIRouter(prefix="/objet", tags=["objet"])

# obtain list of all "objet"
@router_object.get("/")
def get_objects(db = Depends(get_db)):
    try:
        return get_all(db)
    except:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR)

# get a "objet" by id
@router_object.get("/{id}")
def get_object(id: int, db: Session = Depends(get_db)):
    try:
        return get_object_byId(id, db)
    except:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR)

# create a new "objet"
@router_object.post("/create")
def post_object(object: ObjectCreate ,db = Depends(get_db)):
    try:
        return create_object(object, db)
    except:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR)

#  update a "objet" corresponding to the provided id
@router_object.put("/update/{id}")
def put_object(id: int, object: ObjectUpdate, db = Depends(get_db)):
    return update_object(id, object, db)
    # try:
    #     return update_object(id, object, db)
    # except: 
    #     raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR)

# delete the "objet" corresponding to the provided id
@router_object.delete("/{id}/delete")
def delete_object(id: int, db = Depends(get_db)):
    try:
        return delete_object_byId(id, db)
    except:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR)



