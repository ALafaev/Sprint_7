class ResponseText:
    CREATE_COURIER_SUCCESSFULLY = {'ok': True}
    CREATE_COURIER_LOGIN_ALREADY_USED = {'code': 409, 'message': 'Этот логин уже используется. Попробуйте другой.'}
    CREATE_COURIER_NOT_ENOUGH_DATA = {'code': 400, 'message': 'Недостаточно данных для создания учетной записи'}
    LOGIN_COURIER_SUCCESSFULLY_CONTAINS = 'id'
    LOGIN_COURIER_NOT_ENOUGH_DATA = {'code': 400, 'message': 'Недостаточно данных для входа'}
    LOGIN_COURIER_ACCOUNT_NOT_FOUND = {'code': 404, 'message': 'Учетная запись не найдена'}
    MAKE_ORDER_CREATED_CONTAINS = 'track'
