from datetime import date

from fastapi.testclient import TestClient

from midas.main import app


def test_list_categories() -> None:
    with TestClient(app) as client:
        response = client.get("/categories")
        data = response.json()

        assert response.status_code == 200
        assert len(data) == 0


def test_create_category() -> None:
    with TestClient(app) as client:
        response = client.post("/categories", json={"name": "test"})
        data = response.json()

        assert response.status_code == 200
        assert data["id"] == 1
        assert data["name"] == "test"


def test_list_entries() -> None:
    with TestClient(app) as client:
        response = client.get("/entries")
        data = response.json()

        assert response.status_code == 200
        assert len(data) == 0


def test_create_entry() -> None:
    with TestClient(app) as client:
        today = date.today().strftime("%Y-%m-%d")
        client.post("/categories", json={"name": "test"})
        response = client.post(
            "/entries",
            json={
                "description": "test description",
                "value": 10.5,
                "date": today,
                "category_id": 1,
            },
        )
        data = response.json()

        assert response.status_code == 200
        assert data["description"] == "test description"
        assert data["date"] == today
