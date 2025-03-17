import pytest
import requests
from urls import ApiUrls
from helpers import CourierData


@pytest.fixture
def delete_courier():
    yield
    login_data = {
        "login": CourierData.creation_data["login"],
        "password": CourierData.creation_data["password"]
    }
    response = requests.post(ApiUrls.COURIER_LOGIN, data=login_data)
    courier_id = response.json()['id']
    delete_courier_response = requests.delete(ApiUrls.DELETE_COURIER + str(courier_id))
    assert delete_courier_response.status_code == 200


