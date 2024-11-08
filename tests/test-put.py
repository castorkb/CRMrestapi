import requests
from django.contrib.auth import get_user_model

BASE_URL = "http://127.0.0.1:8000/api/workers"  # Замените на правильный базовый URL вашего API

User = get_user_model()

# Получение JWT токена для аутентификации
def get_jwt_token(username, password):
    response = requests.post(f"{BASE_URL}/api/token/", data={
        'username': username,
        'password': password
    })
    return response.json().get('access')


# Тесты для задач
def test_create_task():
    # Создаем пользователя для задачи и получаем токен
    token = get_jwt_token('testuser', 'testpassword')
    headers = {'Authorization': f'Bearer {token}'}

    # Создаем тестовый проект
    project_data = {
        "title": "Test Project",
        "description": "Test Description",
        "deadline": "2025-01-01",
        "status": "in progress"
    }
    project_response = requests.post(f"{BASE_URL}/projects/", headers=headers, json=project_data)
    project_id = project_response.json().get('id')

    # Создаем задачу
    task_data = {
        "task_name": "Test Task",
        "title": "Test Title",
        "description": "Test Description",
        "status": "pending",
        "assigned_to": 1,  # Замените на ID созданного пользователя
        "project": project_id
    }
    response = requests.post(f"{BASE_URL}/tasks/", headers=headers, json=task_data)
    assert response.status_code == 201
    print("Task created:", response.json())


def test_get_task_list():
    # Получаем список задач
    token = get_jwt_token('testuser', 'testpassword')
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.get(f"{BASE_URL}/tasks/", headers=headers)
    assert response.status_code == 200
    print("Task list:", response.json())


def test_get_task_detail(task_id):
    # Получаем детальную информацию о задаче
    token = get_jwt_token('testuser', 'testpassword')
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.get(f"{BASE_URL}/tasks/{task_id}/", headers=headers)
    assert response.status_code == 200
    print("Task detail:", response.json())


def test_update_task(task_id):
    # Обновляем задачу
    token = get_jwt_token('testuser', 'testpassword')
    headers = {'Authorization': f'Bearer {token}'}
    update_data = {
        "task_name": "Updated Task",
        "title": "Updated Title",
        "description": "Updated Description",
        "status": "completed",
        "assigned_to": 1,  # ID пользователя
        "project": 1  # ID проекта
    }
    response = requests.put(f"{BASE_URL}/tasks/{task_id}/", headers=headers, json=update_data)
    assert response.status_code == 200
    print("Task updated:", response.json())


def test_delete_task(task_id):
    # Удаляем задачу
    token = get_jwt_token('testuser', 'testpassword')
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.delete(f"{BASE_URL}/tasks/{task_id}/", headers=headers)
    assert response.status_code == 204
    print("Task deleted")

# Примеры вызовов функций:
if __name__ == "__main__":
    test_create_task()
    test_get_task_list()
    task_id = 1  # Укажите реальный ID задачи, полученный после создания
    test_get_task_detail(task_id)
    test_update_task(task_id)
    test_delete_task(task_id)

