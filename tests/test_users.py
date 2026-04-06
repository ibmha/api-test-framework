
def test_get_users(api_client):
    response = api_client.get("/users")

    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0


def test_get_single_user(api_client):
    response = api_client.get("/users/1")

    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1


def test_title(api_client):
    response = api_client.get("/todos/1")

    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "delectus aut aute"

def test_create_post(api_client):
    payload = {
        "title": "automation",
        "body": "testing",
        "userId": 1
    }

    response = api_client.post("/posts", payload)

    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "automation"