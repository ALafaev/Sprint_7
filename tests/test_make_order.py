import json
import requests
import allure
from helpers import OrderData
from urls import ApiUrls

class TestMakeOrder:

    @allure.title('Проверка: При создании заказа можно выбрать черный цвет самоката')
    @allure.description('Запрос POST на /api/v1/orders со значением BLACK в поле colour вернет 201 Created и track в теле ответа')
    def test_make_order_with_black_colour_return_201_created(self):
        order_data = OrderData.order_data
        order_data['colour'] = OrderData.colour_black
        response = requests.post(ApiUrls.MAKE_ORDER, data=json.dumps(order_data))

        assert response.status_code == 201 and 'track' in response.json(), "Ответ сервера не совпадает с ожидаемым"

    @allure.title('Проверка: При создании заказа можно выбрать серый цвет самоката')
    @allure.description('Запрос POST на /api/v1/orders со значением GREY в поле colour вернет 201 Created и track в теле ответа')
    def test_make_order_with_grey_colour_return_201_created(self):
        order_data = OrderData.order_data
        order_data['colour'] = OrderData.colour_grey
        response = requests.post(ApiUrls.MAKE_ORDER, data=json.dumps(order_data))

        assert response.status_code == 201 and 'track' in response.json(), "Ответ сервера не совпадает с ожидаемым"

    @allure.title('Проверка: При создании заказа можно выбрать оба цвета самоката')
    @allure.description('Запрос POST на /api/v1/orders со обоими цветами в поле colour вернет 201 Created и track в теле ответа')
    def test_make_order_with_both_colour_return_201_created(self):
        order_data = OrderData.order_data
        order_data['colour'] = OrderData.colour_both
        response = requests.post(ApiUrls.MAKE_ORDER, data=json.dumps(order_data))

        assert response.status_code == 201 and 'track' in response.json(), "Ответ сервера не совпадает с ожидаемым"

    @allure.title('Проверка: При создании заказа можно не выбирать цвет самоката')
    @allure.description('Запрос POST на /api/v1/orders с незаполненным полем colour вернет 201 Created и track в теле ответа')
    def test_make_order_with_no_colour_return_201_created(self):
        order_data = OrderData.order_data
        order_data['colour'] = OrderData.colour_none
        response = requests.post(ApiUrls.MAKE_ORDER, data=json.dumps(order_data))

        assert response.status_code == 201 and 'track' in response.json(), "Ответ сервера не совпадает с ожидаемым"