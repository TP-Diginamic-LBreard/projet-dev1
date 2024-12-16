# importer fastapi
from fastapi import FastAPI

from src.database import engine
from src.models import Base
from src.routers.client_router import router_client
from src.routers.object_router import router_object

# definir les routes
app = FastAPI()
app.include_router(router_client)
app.include_router(router_object)

# importer engine(database.py) et Base(models.py)
Base.metadata.create_all(engine)

@app.get("/")
def toto():
    return {"message": "Hello World"}
