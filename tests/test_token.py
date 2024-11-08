import requests

url = "http://127.0.0.1:8000/api/workers/api/token/"
data = {
    "username": "admin",    
    "password": "qwerty"
}
response = requests.post(url, json=data)

if response.status_code == 200:    
    access = response.json().get('access')
    headers = {
        "Authorization": f"Bearer {access}"
    }    
    print('Логин успешен.')
else:
    print('Ошибка при отправке запроса:', response.status_code, response.text)
