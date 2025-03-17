import requests
import allure
from urls import ApiUrls
from helpers import CheckOrdersList

class TestOrderList:

    @allure.title('Проверка: Можно получить список заказов')
    @allure.description('Запрос GET на /api/v1/orders вернет 200 OK и данные о заказах в теле ответа')
    def test_order_list_request_return_200_ok(self):
        response = requests.get(ApiUrls.ORDERS_LIST)

        assert (response.status_code == 200
                and CheckOrdersList.check_response_dict_keys(response)
                and CheckOrdersList.check_orders_dict_keys(response)
                and CheckOrdersList.check_pageinfo_dict_keys(response)
                and CheckOrdersList.check_availablestations_dict_keys(response)), "Ответ сервера не совпадает с ожидаемым"