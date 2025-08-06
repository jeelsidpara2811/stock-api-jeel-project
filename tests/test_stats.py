from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_valid_response():
    response = client.get("/api/stats?ticker=MSFT&start=2023-01-01&end=2023-12-31")
    assert response.status_code == 200
    data = response.json()
    assert "high" in data
    assert "low" in data
    assert "average" in data
    assert "last_close" in data

def test_missing_ticker():
    response = client.get("/api/stats")
    assert response.status_code == 422  # FastAPI returns 422 for missing required query param