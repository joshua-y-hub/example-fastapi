from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    res = client.get("/")
    print(res.json().get("Hello"))
    assert res.json().get("Hello") == "World"
    assert res.status_code == 200

def test_create_user():
    res = client.post("/users/", json={ "email": "jonny@example.com","password": "pass123"})
    print(res.json())
    assert res.status_code == 201
  