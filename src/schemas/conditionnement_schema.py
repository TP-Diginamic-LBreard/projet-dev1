from pydantic import BaseModel

class ConditionnementBase(BaseModel):
    libcondit: str 
    poidscondit: int 
    prixcond: float 
    ordreimp: int = None

# Schema to create a new conditionnement
class ConditionnementCreate(ConditionnementBase):
    pass

# schema to update an conditionnement
class ConditionnementUpdate(BaseModel):
    libcondit: str = None
    poidscondit: int = None
    prixcond: float = None

class ConditionnementRead(ConditionnementBase):
    idcondit: int


