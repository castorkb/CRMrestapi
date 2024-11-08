import requests

url = "http://127.0.0.1:8000/api/workers/inventory/"

# Данные для создания объекта Inventory
data = {
    "item_name": "имя задачи",
    "stock_Level": 100,  # Пример значения для stock_Level
    "purchase_order": 50  # Пример значения для purchase_order
}

# Токен (предположим, что у вас уже есть access_token)
access_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzMxMDU4NDExLCJpYXQiOjE3MzEwNTEyMTEsImp0aSI6IjExZGUwZmFlMzc3OTRhMWRiODE1ODFhZmExZTRkMGYyIiwidXNlcl9pZCI6MX0.koA5jbqmvHfFlESzesGln6zSXtQY-LPvY6PhC1whtg8'

# Добавляем токен в заголовки запроса
headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json'
}

# Отправляем POST запрос с данными и заголовками
response = requests.post(url, json=data, headers=headers)

# Печать ответа
print(response.status_code)  # Печатает статус код ответа (например, 400 Bad Request)
print(response.json())  # Печатает ответ сервера в формате JSON, чтобы увидеть ошибки валидации
