from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from src.main import app
from src.database import get_db
from src.models import Base

# Create an SQLite database in memory
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}, poolclass=StaticPool)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Override the get_db dependency to use the test database
def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

# Create the test database tables
Base.metadata.create_all(bind=engine)

client = TestClient(app)


def test_create():
    response = client.post("/objet/create/", json={
        "libobj": "string",
        "tailleobj": "string",
        "puobj": 0,
        "poidsobj": 0,
        "indispobj": 0,
        "o_imp": 0,
        "o_aff": 0,
        "o_cartp": 0,
        "points": 0,
        "o_ordre_aff": 0
    })
    assert response.status_code == 200
    assert response.json()["codobj"] == 1

# test read by id endpoint
def test_get():
    response = client.get("/objet/1")
    assert response.status_code == 200
    assert response.json()["codobj"] == 1

# test read all
def test_get_all():
    response = client.get("/objet/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

# test update
def update_object():
    response = client.put("/objet/update/1", json={
        "libobj": "update",
        "tailleobj": "string",
        "puobj": 0,
        "poidsobj": 0,
        "indispobj": 0,
        "o_imp": 0,
        "o_aff": 0,
        "o_cartp": 0,
        "points": 0,
        "o_ordre_aff": 0
    })
    assert response.status_code == 200
    assert response.json()["libobj"] == "updated"

# test delete
def delete_object():
    response = client.delete("/objetS/1/delete")
    assert response.status_code == 200