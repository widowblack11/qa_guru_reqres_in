import requests
from pytest_voluptuous import S

from schemas.user import add_user


def test_create_user_ok(base_url):
    body = {
    "name": "morpheus",
    "job": "leader"
}
    response = requests.post(f'{base_url}/api/users', data=body)
    assert response.status_code == 201
    assert S(add_user) == response.json()
    assert response.json()["name"] == "morpheus"


def test_create_user_without_job(base_url):
    body = {
        "name": "morpheus"
    }
    response = requests.post(f'{base_url}/api/users', data=body)
    assert response.status_code == 201
    assert S(add_user) == response.json()






