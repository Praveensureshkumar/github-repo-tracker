def test_create_repo(client):
    response = client.post(
        "/repos",
        json={
            "owner": "fastapi",
            "repo_name": "fastapi"
        }
    )
    assert response.status_code == 201
    data = response.json()
    assert "id" in data
    assert data["owner"] == "fastapi"


def test_get_repo(client):
    create = client.post(
        "/repos",
        json={
            "owner": "psf",
            "repo_name": "requests"
        }
    )
    repo_id = create.json()["id"]

    response = client.get(f"/repos/{repo_id}")
    assert response.status_code == 200
    assert response.json()["id"] == repo_id


def test_update_repo(client):
    create = client.post(
        "/repos",
        json={
            "owner": "pallets",
            "repo_name": "flask"
        }
    )
    repo_id = create.json()["id"]

    response = client.put(
        f"/repos/{repo_id}",
        json={"name": "flask-updated"}
    )
    assert response.status_code == 200
    assert response.json()["name"] == "flask-updated"


def test_delete_repo(client):
    create = client.post(
        "/repos",
        json={
            "owner": "tiangolo",
            "repo_name": "fastapi"
        }
    )
    repo_id = create.json()["id"]

    response = client.delete(f"/repos/{repo_id}")
    assert response.status_code == 204

    check = client.get(f"/repos/{repo_id}")
    assert check.status_code == 404
