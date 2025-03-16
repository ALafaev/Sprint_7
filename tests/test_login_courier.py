import requests
import allure
from helpers import CourierData
from urls import ApiUrls

class TestLoginCourier:

    @allure.title('Проверка: курьер может авторизоваться в системе с существующей парой логин/пароль')
    @allure.description('Запрос POST на /api/v1/courier/login с валидными данными вернет 200 OK')
    def test_courier_login_with_valid_data_return_200_ok(self):
        courier_creation_data = CourierData.creation_data
        requests.post(ApiUrls.COURIER_CREATION, data=courier_creation_data)
        login_data = {
            "login": courier_creation_data["login"],
            "password": courier_creation_data["password"]
        }
        response = requests.post(ApiUrls.COURIER_LOGIN, data=login_data)

        assert response.status_code == 200 and 'id' in response.json(), "Ответ сервера не совпадает с ожидаемым"

    @allure.title('Проверка: курьер не может авторизоваться без передачи значения "login"')
    @allure.description('Запрос POST на /api/v1/courier/login без значения "login" вернет 400 Bad Request')
    def test_courier_login_without_login_return_400_bad_request(self):
        courier_creation_data = CourierData.creation_data
        requests.post(ApiUrls.COURIER_CREATION, data=courier_creation_data)
        login_data = {
            "login": "",
            "password": courier_creation_data["password"]
        }
        response = requests.post(ApiUrls.COURIER_LOGIN, data=login_data)

        assert response.status_code == 400 and response.json() == {'code': 400,
                                                                   'message': 'Недостаточно данных для входа'}, "Ответ сервера не совпадает с ожидаемым"

    @allure.title('Проверка: курьер не может авторизоваться без передачи значения "password"')
    @allure.description('Запрос POST на /api/v1/courier/login без значения "password" вернет 400 Bad Request')
    def test_courier_login_without_password_return_400_bad_request(self):
        courier_creation_data = CourierData.creation_data
        requests.post(ApiUrls.COURIER_CREATION, data=courier_creation_data)
        login_data = {
            "login": courier_creation_data["login"],
            "password": ""
        }
        response = requests.post(ApiUrls.COURIER_LOGIN, data=login_data)

        assert response.status_code == 400 and response.json() == {'code': 400,
                                                                   'message': 'Недостаточно данных для входа'}, "Ответ сервера не совпадает с ожидаемым"

    @allure.title('Проверка: курьер не может авторизоваться, если в запросе отсутствует поле "login"')
    @allure.description('Запрос POST на /api/v1/courier/login, в котором отсутствует поле "login", вернет 400 Bad Request')
    def test_courier_login_no_login_field_return_400_bad_request(self):
        courier_creation_data = CourierData.creation_data
        requests.post(ApiUrls.COURIER_CREATION, data=courier_creation_data)
        login_data = {
            "password": courier_creation_data["password"]
        }
        response = requests.post(ApiUrls.COURIER_LOGIN, data=login_data)

        assert response.status_code == 400 and response.json() == {'code': 400,
                                                                   'message': 'Недостаточно данных для входа'}, "Ответ сервера не совпадает с ожидаемым"

    @allure.title('Проверка: курьер не может авторизоваться, если в запросе отсутствует поле "password"')
    @allure.description('Запрос POST на /api/v1/courier/login, в котором отсутствует поле "password", вернет 400 Bad Request')
    def test_courier_login_no_password_field_return_400_bad_request(self):
        courier_creation_data = CourierData.creation_data
        requests.post(ApiUrls.COURIER_CREATION, data=courier_creation_data)
        login_data = {
            "login": courier_creation_data["login"]
        }
        response = requests.post(ApiUrls.COURIER_LOGIN, data=login_data)

        assert response.status_code == 400 and response.json() == {'code': 400,
                                                                   'message': 'Недостаточно данных для входа'}, "Ответ сервера не совпадает с ожидаемым"

    @allure.title('Проверка: нельзя авторизоваться в системе с существующим логином и несуществующим паролем')
    @allure.description('Запрос POST на /api/v1/courier/login с существующим логином и несуществующим паролем вернет 404 Not Found')
    def test_courier_login_with_wrong_password_return_404_not_found(self):
        courier_creation_data = CourierData.creation_data
        requests.post(ApiUrls.COURIER_CREATION, data=courier_creation_data)
        login_data = {
            "login": courier_creation_data["login"],
            "password": CourierData.wrong_password
        }
        response = requests.post(ApiUrls.COURIER_LOGIN, data=login_data)

        assert response.status_code == 404 and response.json() == {'code': 404,
                                                                   'message': 'Учетная запись не найдена'}, "Ответ сервера не совпадает с ожидаемым"

    @allure.title('Проверка: нельзя авторизоваться в системе с несуществующим логином и существующим паролем')
    @allure.description('Запрос POST на /api/v1/courier/login с несуществующим логином и существующим паролем вернет 404 Not Found')
    def test_courier_login_with_wrong_login_return_404_not_found(self):
        courier_creation_data = CourierData.creation_data
        requests.post(ApiUrls.COURIER_CREATION, data=courier_creation_data)
        login_data = {
            "login": CourierData.wrong_login,
            "password": courier_creation_data["password"]
        }
        response = requests.post(ApiUrls.COURIER_LOGIN, data=login_data)

        assert response.status_code == 404 and response.json() == {'code': 404,
                                                                   'message': 'Учетная запись не найдена'}, "Ответ сервера не совпадает с ожидаемым"