import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.models import Base, Client
from src.main import app
from src.database import get_db

# Configuration pour utiliser une base de données SQLite en mémoire
DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dépendance overridée pour utiliser SQLite en mémoire
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)

# Fixture pour initialiser et nettoyer la base de données pour chaque test
@pytest.fixture(autouse=True)
def setup_db():
    Base.metadata.create_all(bind=engine)  # Crée les tables
    yield
    Base.metadata.drop_all(bind=engine)  # Supprime les tables après chaque test

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
