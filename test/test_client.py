from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.main import app
from src.database import get_db
from src.models import Base

# Create an SQLite database in memory
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
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

# ========================= TESTS CRUD ==========================

# Test CREATE
def test_create_client():
    response = client.post("/client/", json={"nomcli": "Clairet", "prenomcli": "Rémy"})
    assert response.status_code == 200
    assert response.json()["nomcli"] == "CLAIRET"  # Vérifie la mise en majuscules

# Test READ ALL
def test_read_all_clients():
    client.post("/client/", json={"nomcli": "Clairet", "prenomcli": "Rémy"})
    response = client.get("/client/")
    assert response.status_code == 200
    assert len(response.json()) == 1

# Test READ BY ID
def test_read_client_by_id():
    # Crée un client
    response_create = client.post("/client/", json={"nomcli": "Clairet", "prenomcli": "Rémy"})
    assert response_create.status_code == 200
    client_id = response_create.json()["id"]  # Récupère l'ID renvoyé

    # Test READ BY ID
    response = client.get(f"/client/{client_id}")
    assert response.status_code == 200
    assert response.json()["nomcli"] == "CLAIRET"

def test_delete_client():
    # Crée un client
    response_create = client.post("/client/", json={"nomcli": "Clairet", "prenomcli": "Rémy"})
    assert response_create.status_code == 200
    client_id = response_create.json()["id"]

    # Test DELETE
    response = client.delete(f"/client/{client_id}")
    assert response.status_code == 200
    assert response.json()["message"] == "Utilisateur supprimé"

    # Vérifie que le client n'existe plus
    response = client.get(f"/client/{client_id}")
    assert response.status_code == 404