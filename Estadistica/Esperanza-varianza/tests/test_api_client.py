from fastapi.testclient import TestClient
from api import app


client = TestClient(app)


def test_get_stats():
    r = client.get("/stats", params={"values": "1,2,3,4"})
    assert r.status_code == 200
    data = r.json()
    assert "esperanza" in data and "varianza" in data


def test_post_stats():
    r = client.post("/stats", json={"values": [1, 2, 3, 4]})
    assert r.status_code == 200
    data = r.json()
    assert data["esperanza"] == 2.5


def test_plot_png():
    r = client.get("/plot.png", params={"values": "1,2,3,4"})
    assert r.status_code == 200
    assert r.headers["content-type"].startswith("image/png")
    assert r.content[:8] == b"\x89PNG\r\n\x1a\n"


def test_explain():
    r = client.get("/explain")
    assert r.status_code == 200
    data = r.json()
    assert "explanation" in data
