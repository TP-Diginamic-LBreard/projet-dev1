from fastapi import APIRouter, Depends, HTTPException, status, Form
from sqlalchemy.orm import Session
from src.database import get_db
from src.services.objet_service import get_all, get_object_byId, delete_object_byId, create_object, update_object
from src.schemas.object_schema import ObjectSchema


# le tag permet d'organiser les endpoint dans la doc
router_object = APIRouter(prefix="/objet", tags=["objet"])

@router_object.get("/")
def get_objects(db = Depends(get_db)):
    try:
        return get_all(db)
    except:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@router_object.get("/{id}")
def get_object(id: int, db: Session = Depends(get_db)):
    try:
        return get_object_byId(id, db)
    except:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@router_object.post("/create")
def post_object(object: ObjectSchema ,db = Depends(get_db)):
    return create_object(object, db)


@router_object.put("/update/{id}")
def put_object(id: int, new_libobj: str, db = Depends(get_db)):
    return update_object(id, new_libobj, db)

@router_object.delete("/{id}/delete")
def delete_object(id: int, db = Depends(get_db)):
    try:
        return delete_object_byId(id, db)
    except:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR)



