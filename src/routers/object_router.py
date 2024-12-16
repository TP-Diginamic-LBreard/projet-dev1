from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from src.database import get_db
from src.services.objet_service import get_all, get_object_byID


# le tag permet d'organiser les endpoint dans la doc
router_object = APIRouter(prefix="/objet", tags=["objet"])

@router_object.get("/")
def read_object(db = Depends(get_db)):
    try:
        return get_all(db)
    except:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@router_object.get("/{id}")
def read_object(id: int, db: Session = Depends(get_db)):
    try:
        return get_object_byID(db)
    except:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR)



