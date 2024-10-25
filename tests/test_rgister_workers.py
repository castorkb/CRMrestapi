import requests

data = {
    "username": "бро",
    "email": "adila@gmail.com",
    "password": "123321456654",
    "group": "Геодезист"
}

# Отправка POST-запроса на сервер
response = requests.post('http://127.0.0.1:8000/api/workers/register/', json=data)
# Проверка статуса ответа
if response.status_code == 201: # 201 означает, что ресурс успешно создан
    print('User created successfully')
    user = response.json() # Получаем данные о созданном пользователе
    print(user)

else:
    print(f'Failed to create user. Status code: {response.status_code}')