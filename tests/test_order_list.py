import requests
import allure
from urls import ApiUrls

class TestOrderList:

    @allure.title('Проверка: Можно получить список заказов')
    @allure.description('Запрос GET на /api/v1/orders вернет 200 OK и данные о заказах в теле ответа')
    def test_order_list_request_return_200_ok(self):
        response_dict_keys = ["orders", "pageInfo", "availableStations"]
        orders_dict_keys = ["id", "courierId", "firstName", "lastName", "address", "metroStation", "phone", "rentTime", "deliveryDate", "track", "color", "comment", "createdAt", "updatedAt", "status"]
        pageinfo_dict_keys = ["page", "total", "limit"]
        availablestations_dict_keys = ["name", "number", "color"]
        response = requests.get(ApiUrls.ORDERS_LIST)

        assert (response.status_code == 200
                and all(key in response_dict_keys for key in response.json().keys())
                and all(key in orders_dict_keys for key in response.json()['orders'][0])
                and all(key in pageinfo_dict_keys for key in response.json()['pageInfo'])
                and all(key in availablestations_dict_keys for key in response.json()['availableStations'][0])), "Ответ сервера не совпадает с ожидаемым"