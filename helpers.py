from faker import Faker
import random, datetime

fake_courier = Faker(locale="ru_RU")
courier_firstName = fake_courier.first_name_male()
courier_password = random.randint(1000, 9999)
courier_login = fake_courier.user_name()

class CourierData:
    creation_data = {
        "login": courier_login,
        "password": courier_password,
        "firstName": courier_firstName
    }
    creation_data_without_login_value = {
        "login": '',
        "password": courier_password,
        "firstName": courier_firstName
    }
    creation_data_without_password_value = {
        "login": courier_login,
        "password": '',
        "firstName": courier_firstName
    }
    creation_data_without_login_field = {
        "password": courier_password,
        "firstName": courier_firstName
    }
    creation_data_without_password_field = {
        "login": courier_login,
        "firstName": courier_firstName
    }
    wrong_login = 'Qwerty'
    wrong_password = 'qwerty'

fake_client = Faker(locale="ru_RU")

today = datetime.date.today()
tomorrow = today + datetime.timedelta(days=1)
date = random.choice((today, tomorrow))
deliveryDate = date.strftime('%d.%m.%Y')

class OrderData:
    colour_black = ["BLACK"]
    colour_grey = ["GREY"]
    colour_both = ["BLACK", "GREY"]
    colour_none = []

    order_data = {
        "firstName": fake_client.first_name(),
        "lastName": fake_client.last_name(),
        "address": fake_client.address(),
        "metroStation": random.randint(1,10),
        "phone": fake_client.phone_number(),
        "rentTime": random.randint(1,7),
        "deliveryDate": deliveryDate,
        "comment": fake_client.text(max_nb_chars=40),
    }
