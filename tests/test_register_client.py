import requests

data = {
    "username": "Ivan",
    "first_name": "Иван",
    "last_name": "Иванов",
    "email": "adil@gmail.com",
    "phone_number": "+79123456789",
    "password": "567156",
    "group": "Клиенты"
}

# Отправка POST-запроса на сервер
response = requests.post('http://127.0.0.1:8000/api/client/register/', json=data)
# Проверка статуса ответа
if response.status_code == 201: # 201 означает, что ресурс успешно создан
    print('Пользователь успешно создан')
    user = response.json() # Получаем данные о созданном пользователе
    print(user)

else:
    print(f'Не удалось создать пользователя. Код состояния: {response.status_code}')