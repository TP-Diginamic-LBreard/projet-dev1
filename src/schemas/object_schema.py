from pydantic import BaseModel

# Schema to create a new object
class ObjectCreate(BaseModel):
    codobj: int
    libobj: str
    tailleobj: str
    puobj: float = None
    poidsobj: float
    indispobj: int = None
    o_imp: int = None
    o_aff: int = None
    o_cartp: int = None
    points: int
    o_ordre_aff: int = None

# schema to update an object
class ObjectUpdate(BaseModel):
    codobj: int 
    libobj: str = None 
    tailleobj: str = None
    puobj: float = None
    poidsobj: float = None
    indispobj: int = None
    o_imp: int = None
    o_aff: int = None
    o_cartp: int = None
    points: int = None
    o_ordre_aff: int = None