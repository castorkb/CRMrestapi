import requests

url = "http://127.0.0.1:8000/api/workers/resources/"

# Данные для создания объекта Inventory
data = {
    "name": "Название ресурса", # Название ресурса ('Цемент', 'Бетон', и т. д.)
    "type": " Строительный материал",  # Тип ресурса ('Строительный материал', 'Оборудование', и т. д.)
    "quantity": "100 кг",  # Количество ресурса (100 кг, 50 штук и т. д.)
    "availability": "В наличии",  # Доступность ресурса ('В наличии', 'Нет в наличии', и т. д.)
    "usage_history": "Используется на проекте A",  # История использования ресурса ('Используется на проекте A', 'Использовался в проекте B' и т. д.)

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