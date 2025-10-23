import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                '..')))

from fastapi.testclient import TestClient

from main import app



client = TestClient(app)


def test_read_sheep():
    response = client.get("/sheep/1")

    assert response.status_code == 200

    assert response.json() == {
        "id":1,
        "name": "Spice",
        "breed": "Gotland",
        "sex": "ewe"
    }






#define a test function for adding a new sheep
def test_add_sheep():
    #TODO: prepare the new sheep data in the dictionary format
    new_sheep = {
        "id": 7,
        "name": "Suffolk",
        "breed": "Polypay",
        "sex": "ewe"
    }

    #TODO: Send a POST request to the endpoint "/sheep" with the new sheep data
    #Arguments should be your endpoint and new sheep data.
    response = client.post("/sheep", json=new_sheep)

    #TODO: Assert that the response status code is 201 (Created)
    assert response.status_code == 201

    #TODO: Assert that the response JSON matches the new sheep data
    assert response.json() == new_sheep

    #TODO: Verify that the sheep was actually added to the database by retrieving the new sheep by ID.
    #include an assert statement to see fi the new sheep data can be retrieved.
    get_response = client.get("/sheep/2")
    assert get_response.status_code == 200
    assert get_response.json() == new_sheep


def test_read_sheep():
    client.post("/sheep/", json={"id": 2, "name": "Molly", "age": 3})
    response = client.get("/sheep/2")
    assert response.status_code == 200
    assert response.json()["name"] == "Molly"

def test_update_sheep():
    client.post("/sheep/", json={"id": 3, "name": "Polly", "age": 1})
    response = client.put("/sheep/3", json={"id": 3, "name": "Polly", "age": 2})
    assert response.status_code == 200
    assert response.json()["age"] == 2

def test_delete_sheep():
    client.post("/sheep/", json={"id": 4, "name": "Lolly", "age": 2})
    response = client.delete("/sheep/4")
    assert response.status_code == 204
    # Confirm deletion
    response = client.get("/sheep/4")
    assert response.status_code == 404

def test_read_all_sheep():
    # Ensure at least one sheep exists
    client.post("/sheep/", json={"id": 5, "name": "Tolly", "age": 4})
    response = client.get("/sheep/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert any(s["id"] == 5 for s in response.json())