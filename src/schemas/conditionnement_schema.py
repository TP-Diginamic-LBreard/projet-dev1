from pydantic import BaseModel

# Schema to create a new conditionnement
class ConditionnementCreate(BaseModel):
    idcondit: int 
    libcondit: str 
    poidscondit: int 
    prixcond: float 
    ordreimp: int = None
# schema to update an conditionnement
class ConditionnementUpdate(BaseModel):
    idcondit: int 
    libcondit: str = None
    poidscondit: int = None
    prixcond: float = None
    ordreimp: int = None
