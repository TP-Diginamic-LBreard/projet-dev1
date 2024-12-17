from pydantic import BaseModel
from typing import Optional

# Modèle Pydantic pour Client
class ClientSchema(BaseModel):
    codcli: int
    genrecli: Optional[str] = None
    nomcli: str
    prenomcli: Optional[str] = None
    adresse1cli: Optional[str] = None
    telcli: Optional[str] = None
    emailcli: Optional[str] = None

    class Config:
        from_attributes = True  # Remplacer `orm_mode` pour Pydantic v2
