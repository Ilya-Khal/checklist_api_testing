import configuration
import requests
import data

# Определение функции post_new_user для отправки POST-запроса на создание нового пользователя
def post_new_user(body):

    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)
def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)


response = get_users_table()

# Вызов функции post_new_user с телом запроса для создания нового пользователя из модуля data





response = post_new_user(data.user_body);


print(response.status_code)

print(response.json())
