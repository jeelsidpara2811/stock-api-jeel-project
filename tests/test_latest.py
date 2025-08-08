from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_latest_valid_ticker():
    response = client.get("/api/latest?ticker=AAPL")
    assert response.status_code == 200
    data = response.json()
    assert "last_close" in data
    assert "change" in data
    assert "change_percent" in data

def test_latest_invalid_ticker():
    response = client.get("/api/latest?ticker=INVALID123")
    assert response.status_code == 404
    assert response.json()["detail"] == "Unable to retrieve latest price"
