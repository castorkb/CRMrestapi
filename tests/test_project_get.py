import requests

# URL API для создания проекта
url = "http://127.0.0.1:8000/api/workers/projects/"

# Данные для проекта
data = {
    "Title": "New Project",
    "Description": "Description of the new project",
    "Deadline": "2024-12-31",
    "Status": "In Progress",
    "manager": 1,  # ID менеджера
    "client": 2,   # ID клиента
    "team": [1] # Список ID членов команды
}

# JWT токен авторизации
headers = {

    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI5ODYzOTU4LCJpYXQiOjE3Mjk4NjM2NTgsImp0aSI6IjBkYmM3MmE5ZDM5NTRmZWJiNjMxMjJjOTliYjI2NThkIiwidXNlcl9pZCI6MX0.XwyZnD-qQkyeze7D_ICQhPCpesANzszmsWBJMAk3urk",
    "Content-Type": "application/json"
}

# Отправляем POST-запрос для создания проекта
response = requests.post(url, json=data, headers=headers)

# Выводим статус ответа и данные
print(response.status_code)
print(response.json())

