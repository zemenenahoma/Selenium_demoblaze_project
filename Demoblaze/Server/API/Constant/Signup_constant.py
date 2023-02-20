from random import randint

class RegisterConstants:
    num = randint(1, 2500)
    url_register = 'https://api.demoblaze.com/signup'
    data_valid = {'user_name': "yeshiva",
                  'password': "yeshubel1427"}

    data_exist_password = {'name': "hana",
                             'password': "yeshubel1427"}

    data_exist_username = {'name': "yeshiva",
                             'password': "kjhgfd"}

    data_exist_passwored_and_username = {'name': " yeshiva",
                                    'password': "yeshubel1427"}

    data__empty_passwerd_and_username = {'name': "",
                                   'password': ""}

