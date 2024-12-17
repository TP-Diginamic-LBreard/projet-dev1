from pydantic import BaseModel

class ObjectBase(BaseModel):
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

# Schema to create a new object
class ObjectCreate(ObjectBase):
    pass

# schema to update an object
class ObjectUpdate(ObjectBase):
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

class ObjectRead(ObjectBase):
    codobj: int