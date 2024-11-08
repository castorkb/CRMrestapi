import requests

url = "http://127.0.0.1:8000/api/workers/tasks/"

# Пустой запрос
data = {
    "task_name": "имя задачи1",
    "title": "заголовок",
    "description": "описание",
    "status": "статус",
    "assigned_to": 17,
    "project": 5,
}

response = requests.post(url, json=data)

# Печать ответа
print(response.status_code)  # Печатает статус код ответа (например, 400 Bad Request)
print(response.json())  # Печатает ответ сервера в формате JSON, чтобы увидеть ошибки валидации




