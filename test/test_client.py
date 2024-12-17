from fastapi.testclient import TestClient
from src.main import app


client = TestClient(app)

# changer de base de données : sqlite
# pour notre cas pas besoin de changer de bdd

# Test pour les 2 fonctions get (GET)
def test_get_all_clients():
    response = client.get("/client/")
    assert response.status_code == 200 # success
    assert isinstance(response.json(), list)

def test_get_client_by_id():
    # Simule une requête GET pour un client existant (exemple avec ID 1)
    response = client.get("/client/1")
    assert response.status_code == 200  # On vérifie que la réponse est un succès
    assert "nomcli" in response.json()  # On vérifie que le champ 'nomcli' est présent dans la réponse
    assert response.json()["codcli"] == 1  # On vérifie que l'ID retourné correspond

# Test pour create_client (POST)
def test_create_client():
    # Simule une requête POST avec des données pour créer un client
    new_client = {
        "genrecli": "Mme",
        "nomcli": "Dupont",
        "prenomcli": "Marie",
        "adresse1cli": "10 Rue des Lilas",
        "telcli": "0123456789",
        "emailcli": "marie.dupont@example.com",
    }
    response = client.post("/client/", json=new_client)
    assert response.status_code == 201  # Code 201 pour création réussie
    assert response.json()["nomcli"] == "Dupont"

# Test pour update_client (PUT)
def test_update_client():
    updated_client = {
        "genrecli": "M.",
        "nomcli": "Durand",
        "prenomcli": "Jean",
        "adresse1cli": "20 Avenue de la Paix",
        "telcli": "0987654321",
    }
    response = client.put("/client/1", json=updated_client)  # Exemple avec ID 1
    assert response.status_code == 200
    assert response.json()["nomcli"] == "Durand"

# Test pour delete_client (DELETE)
def test_delete_client():
    response = client.delete("/client/1")  # Exemple avec ID 1
    assert response.status_code == 204  # Code 204 pour suppression réussie

# Test non passant 
def test_get_client_by_id_not_found():
    # Simule une requête GET pour un client qui n'existe pas
    response = client.get("/client/9999")  # ID inexistant
    assert response.status_code == 404  # On s'attend à une erreur 404
