import requests
from pytest_voluptuous import S

from schemas.user import update_user


def test_update_info_about_user_ok(base_url):
    body = {
    "name": "morpheus",
    "job": "leader"
}
    response = requests.patch(f'{base_url}/api/users/2', data=body)
    assert response.status_code == 200
    assert S(update_user) == response.json()
    assert response.json()["name"] == "morpheus" and response.json()["job"] == "leader"


def test_update_info_about_user_when_user_not_found(base_url):
    body = {
    "name": "morpheus",
    "job": ["leader", "teacher",]
}
    response = requests.patch(f'{base_url}/api/users/2', data=body)
    assert response.status_code == 200
    assert S(update_user) == response.json()
