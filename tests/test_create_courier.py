import requests
import allure
from helpers import CourierData
from urls import ApiUrls

class TestCreateCourier:

    @allure.title('Проверка: можно создать курьера')
    @allure.description('Запрос POST на /api/v1/courier с валидными данными вернет 201 Created')
    def test_courier_creation_with_valid_data_return_201_created(self):
        courier_creation_data = CourierData.creation_data
        response = requests.post(ApiUrls.COURIER_CREATION, data=courier_creation_data)

        assert response.status_code == 201 and response.json() == {'ok': True}, "Ответ сервера не совпадает с ожидаемым"

    @allure.title('Проверка: нельзя создать двух одинаковых курьеров')
    @allure.description('Повторный POST запрос на /api/v1/courier с такими же данными вернет 409 Conflict')
    def test_courier_creation_with_the_same_data_return_409_conflict(self):
        courier_creation_data = CourierData.creation_data
        requests.post(ApiUrls.COURIER_CREATION, data=courier_creation_data)
        response = requests.post(ApiUrls.COURIER_CREATION, data=courier_creation_data)

        assert response.status_code == 409 and response.json() == {'code': 409, 'message': 'Этот логин уже используется. Попробуйте другой.'}, "Ответ сервера не совпадает с ожидаемым"

    @allure.title('Проверка: нельзя создать курьера без значения "login"')
    @allure.description('Запрос POST на /api/v1/courier с незаполненным полем "login" вернет 400 Bad Request')
    def test_courier_creation_without_login_value_return_400_bad_request(self):
        courier_creation_data = CourierData.creation_data_without_login_value
        response = requests.post(ApiUrls.COURIER_CREATION, data=courier_creation_data)

        assert response.status_code == 400 and response.json() == {'code': 400, 'message': 'Недостаточно данных для создания учетной записи'}, "Ответ сервера не совпадает с ожидаемым"

    @allure.title('Проверка: нельзя создать курьера без значения "password"')
    @allure.description('Запрос POST на /api/v1/courier с незаполненным полем "password" вернет 400 Bad Request')
    def test_courier_creation_without_password_value_return_400_bad_request(self):
        courier_creation_data = CourierData.creation_data_without_password_value
        response = requests.post(ApiUrls.COURIER_CREATION, data=courier_creation_data)

        assert response.status_code == 400 and response.json() == {'code': 400, 'message': 'Недостаточно данных для создания учетной записи'}, "Ответ сервера не совпадает с ожидаемым"

    @allure.title('Проверка: нельзя создать курьера, если в запросе отсутствует поле "login"')
    @allure.description('Запрос POST на /api/v1/courier с отсутствующим полем "login" вернет 400 Bad Request')
    def test_courier_creation_without_login_field_return_400_bad_request(self):
        courier_creation_data = CourierData.creation_data_without_login_field
        response = requests.post(ApiUrls.COURIER_CREATION, data=courier_creation_data)

        assert response.status_code == 400 and response.json() == {'code': 400,
                                                                   'message': 'Недостаточно данных для создания учетной записи'}, "Ответ сервера не совпадает с ожидаемым"

    @allure.title('Проверка: нельзя создать курьера, если в запросе отсутствует поле "password"')
    @allure.description('Запрос POST на /api/v1/courier с отсутствующим полем "password" вернет 400 Bad Request')
    def test_courier_creation_without_password_field_return_400_bad_request(self):
        courier_creation_data = CourierData.creation_data_without_password_field
        response = requests.post(ApiUrls.COURIER_CREATION, data=courier_creation_data)

        assert response.status_code == 400 and response.json() == {'code': 400,
                                                                   'message': 'Недостаточно данных для создания учетной записи'}, "Ответ сервера не совпадает с ожидаемым"


