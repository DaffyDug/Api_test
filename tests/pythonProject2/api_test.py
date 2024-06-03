import requests
BASE_URL = 'https://reqres.in/api'
def get_request():
    response = requests.get(f'{BASE_URL}/users')
    return response
def get_user_id(user_id):
    response = requests.get(f'{BASE_URL}/users/{user_id}')
    return response
def post_user(name, job):
    json_data = {"name": name, "job": job}
    response = requests.get(f'{BASE_URL}/users', json = json_data)
    return response
def put_user(user_id, name, job):
    json_data = {"name": name, "job": job}
    response = requests.put(f'{BASE_URL}/users/{user_id}', json = json_data)
    return response
def delete_user(user_id):
    response = requests.delete(f'{BASE_URL}/users/{user_id}')
    return response