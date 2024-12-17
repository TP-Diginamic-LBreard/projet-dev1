from fastapi import status
from fastapi.testclient import TestClient
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from src.main import app
from src.database import get_db
from src.models import Base, Client, Commande


engine = create_engine("sqlite:///:memory:", connect_args={"check_same_thread": False}, poolclass=StaticPool)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

def override_db():
    with SessionLocal() as db:
        yield db

app.dependency_overrides[get_db] = override_db
Base.metadata.create_all(bind=engine)

with SessionLocal() as db:
    from datetime import date

    db.add_all([
        Client(
            codcli    = 0,
            nomcli    = "Nyme",
            prenomcli = "Ano"
        ),
        Client(
            nomcli    = "Gnito",
            prenomcli = "Inco"
        ),
    ])

    db.add_all([
        Commande(
            datcde    = date.fromisoformat("2024-12-17"),
            codcli    = 0,
            timbrecli = 0,
            timbrecde = 0,
            cheqcli   = 0
        ),
        Commande(
            datcde    = date.fromisoformat("2024-12-16"),
            codcli    = 0,
            timbrecli = 0,
            timbrecde = 0,
            cheqcli   = 0
        ),
        Commande(
            datcde    = date.fromisoformat("2024-12-15"),
            codcli    = 0,
            timbrecli = 0,
            timbrecde = 0,
            cheqcli   = 0
        ),
    ])

    db.commit()


@pytest.fixture()
def client():
    yield TestClient(app)


class TestCommande:
    def test_get_all(self, client):
        response = client.get("/commande")
        assert response.status_code == status.HTTP_200_OK
        assert isinstance(response.json(), list)


    def test_get_one(self, client):
        response = client.get("/commande/1")
        assert response.status_code == status.HTTP_200_OK

        json = response.json()
        assert json["id"] == 1
        assert json["client"] == 0


    def test_get_one_missing(self, client):
        response = client.get("/commande/10")
        assert response.status_code == status.HTTP_404_NOT_FOUND


    def test_post(self, client):
        response = client.post("/commande", json={
            "date": "2024-11-14",
            "client": 1,
            "timbre_client": 0,
            "timbre_commande": 0,
            "nombre_colis": 1,
            "cheque": 0,
            "conditionnement": 0
        })
        assert response.status_code == status.HTTP_201_CREATED

        new = response.text.split("/")[-1]
        with SessionLocal() as db:
            assert db.get(Commande, new) is not None


    def test_put_create(self, client):
        response = client.put("/commande", json={
            "id": 5,
            "date": "2024-11-14",
            "client": 1,
            "timbre_client": 0,
            "timbre_commande": 0,
            "nombre_colis": 1,
            "cheque": 0,
            "conditionnement": 0
        })
        assert response.status_code == status.HTTP_201_CREATED

        new = response.text.split("/")[-1]
        with SessionLocal() as db:
            assert db.get(Commande, new) is not None


    def test_put_replace(self, client):
        response = client.put("/commande", json={
            "id": 1,
            "date": "2024-11-14",
            "client": 1,
            "timbre_client": 0,
            "timbre_commande": 0,
            "nombre_colis": 1,
            "cheque": 0,
            "conditionnement": 0
        })
        assert response.status_code == status.HTTP_204_NO_CONTENT

        with SessionLocal() as db:
            assert db.get(Commande, 1).datcde.isoformat() == "2024-11-14"


    def test_patch(self, client):
        response = client.patch("/commande/2", json={"client": 1})
        assert response.status_code == status.HTTP_204_NO_CONTENT

        with SessionLocal() as db:
            assert db.get(Commande, 2).codcli == 1


    def test_patch_missing(self, client):
        response = client.patch("/commande/10", json={})
        assert response.status_code == status.HTTP_404_NOT_FOUND


    def test_delete(self, client):
        response = client.delete("/commande/2")
        assert response.status_code == status.HTTP_204_NO_CONTENT

        with SessionLocal() as db:
            assert db.get(Commande, 2) is None


    def test_delete_missing(self, client):
        response = client.delete("/commande/10")
        assert response.status_code == status.HTTP_404_NOT_FOUND
