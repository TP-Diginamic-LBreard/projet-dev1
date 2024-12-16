from pydantic import BaseModel

class ConditionnementCreate(BaseModel):
    idcondit: int 
    libcondit: str 
    poidscondit: int 
    prixcond: float 
    ordreimp: int = None
class ConditionnementUpdate(BaseModel):
    idcondit: int 
    libcondit: str = None
    poidscondit: int = None
    prixcond: float = None
    ordreimp: int = None
