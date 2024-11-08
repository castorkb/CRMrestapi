import requests

# URL для создания нового взаимодействия
url = "http://127.0.0.1:8000/api/client/interactions/"

# Данные для создания нового взаимодействия
data = {
    "manager": 17,  # ID пользователя, который является менеджером (например, ID 5)
    "client": 26,  # ID пользователя, который является клиентом (например, ID 26)
    "type": "Звонок",  # Например, тип взаимодействия "Звонок"
    "details": "Обсуждение условий контракта"  # Описание взаимодействия
}

# Access токен
access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzMxMDc3MjIyLCJpYXQiOjE3MzEwNzAwMjIsImp0aSI6IjU2MDNlOTVhNzdkZjRjYzBhNDIwYjI2NzkyOTAyMzY4IiwidXNlcl9pZCI6MTd9.Su3pP4t33m_aemQlWWvoZZ_SJgf_24HQJdYbZy2BNoc"
# Заголовки с токеном авторизации
headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json'
}

# Отправка POST запроса
response = requests.post(url, json=data, headers=headers)

# Вывод статуса и ответа сервера
print(response.status_code)  # Выводит статус код (например, 201 при успешном создании)
try:
    print(response.json())  # Выводит ответ в формате JSON для проверки
except ValueError:
    print("Ответ сервера не содержит JSON.")
