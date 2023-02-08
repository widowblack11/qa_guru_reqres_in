import pytest

BASE_URL = 'https://reqres.in'


@pytest.fixture()
def base_url():
    return BASE_URL
