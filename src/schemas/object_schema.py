from pydantic import BaseModel

class ObjectSchema(BaseModel):
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