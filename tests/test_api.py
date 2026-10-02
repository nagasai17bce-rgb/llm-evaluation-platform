from fastapi.testclient import TestClient
from app.main import app
client=TestClient(app)
def test_regression_gate(): assert client.post("/v1/run",json={"value":"DEMO"}).json()["regression_gate"] is True
