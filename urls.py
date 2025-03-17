class BaseUrls:
    BASE_URL = "https://qa-scooter.praktikum-services.ru"

class ApiUrls:
    COURIER_CREATION = BaseUrls.BASE_URL + '/api/v1/courier'
    COURIER_LOGIN = BaseUrls.BASE_URL + '/api/v1/courier/login'
    MAKE_ORDER = BaseUrls.BASE_URL + '/api/v1/orders'
    ORDERS_LIST = BaseUrls.BASE_URL + '/api/v1/orders'
    DELETE_COURIER = BaseUrls.BASE_URL + '/api/v1/courier/'
