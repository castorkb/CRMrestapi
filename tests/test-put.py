import requests

# Замените эти значения на свои данные
base_url = 'http://127.0.0.1:8000/api/workers/projects'  # URL вашего API
token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzMwMjk2NjY0LCJpYXQiOjE3MzAyOTYzNjQsImp0aSI6ImUxYzQ5MzFjZTU3NjQ3ZmRiOWNiNDIyMDhkNmVlZDc5IiwidXNlcl9pZCI6MX0.gU8mI3pbIELxoMDAsZjdB3VAtNNUhzUAM-gat5YMJlo'  # Ваш JWT-токен
project_id = 1  # ID проекта
user_id_to_add = 5  # ID пользователя для добавления
user_id_to_remove = 3  # ID пользователя для удаления

# Заголовки с авторизацией
headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json'  # Убедитесь, что указываете тип контента
}

# Запрос на добавление сотрудника в команду проекта
add_team_member_url = f'{base_url}/{project_id}/add_team_member/'
add_data = {'user_id': user_id_to_add}

response_add = requests.post(add_team_member_url, headers=headers, json=add_data)

if response_add.status_code == 200:
    print("Сотрудник добавлен:", response_add.json())
else:
    print("Ошибка при добавлении сотрудника:", response_add.status_code, response_add.json())

# Запрос на удаление сотрудника из команды проекта
remove_team_member_url = f'{base_url}/{project_id}/remove_team_member/'
remove_data = {'user_id': user_id_to_remove}

response_remove = requests.post(remove_team_member_url, headers=headers, json=remove_data)

if response_remove.status_code == 200:
    print("Сотрудник удален:", response_remove.json())
else:
    print("Ошибка при удалении сотрудника:", response_remove.status_code, response_remove.json())
