from random import randint


class LoginConstants:
    num = randint(1, 2500)
    url_login = 'https://api.demoblaze.com/login'
    success_key = 'success'
    message_key = 'message'
    data_valid = {"email": "belsho", "password": f"bela@{123}"}
    data_invalid_password = {"email": "belsho", "password": "123edsdf"}
    data_invalid_email = {"email": "m@fg", "password": "123456"}
    data_invalid_password_and_email = {"email": "m@fg", "password": "bela@123"}
    data_null_password_and_email = {"email": "", "password": ""}