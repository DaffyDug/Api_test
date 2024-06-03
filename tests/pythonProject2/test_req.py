import pytest
from api_test import *

def test_get_users():
    response = get_request()
    assert response.status_code == 200
    assert "data" in response.json()
def test_get_users_id():
    response = get_user_id(2)
    assert response.status_code == 200
    assert response.json()['data']['id'] == 2

def test_negative():
    response = get_user_id(345)
    assert response.status_code == 404
def test_post_users():
    response = post_user("Alice", "singer")
    assert response.status_code_code == 201
    assert response.json()['name'] == 'Alice'
    assert response.json()['job'] == 'singer'
def test_put_user():
    response = put_user(4,'John','developer')
    assert response.status_code == 200
    assert response.json()['name'] == 'John'
    assert response.json()['job'] == 'developer'
def test_delete_user():
    response = delete_user(3)
    assert response.status_code == 204
