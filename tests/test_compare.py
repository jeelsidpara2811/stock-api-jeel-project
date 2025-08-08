from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_compare_valid_tickers():
    response = client.get("/api/compare?ticker1=MSFT&ticker2=AAPL&start=2023-01-01&end=2023-12-31")
    assert response.status_code == 200
    data = response.json()
    assert "MSFT" in data
    assert "AAPL" in data
    assert "high" in data["MSFT"]
    assert "high" in data["AAPL"]

def test_compare_one_invalid_ticker():
    response = client.get("/api/compare?ticker1=MSFT&ticker2=INVALIDXYZ&start=2023-01-01&end=2023-12-31")
    assert response.status_code == 200  # still OK because MSFT is valid
    data = response.json()
    assert "MSFT" in data
    assert "INVALIDXYZ" in data
    assert "error" in data["INVALIDXYZ"]

def test_compare_both_invalid():
    response = client.get("/api/compare?ticker1=XXX123&ticker2=YYY456&start=2023-01-01&end=2023-12-31")
    assert response.status_code == 404
    assert response.json()["detail"] == "No data found for either ticker"
