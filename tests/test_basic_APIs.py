import pytest
from typing import Generator
from playwright.sync_api import Playwright, APIRequestContext

import requests
import random
import pytest

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_GET_todo_status_code():
    response = requests.get(f"{BASE_URL}/todos/1")
    assert response.status_code == 200
    
    
def test_POST_with_bearer_token_public_endpoint():
    url = "https://jsonplaceholder.typicode.com/posts"
    bearer_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyLCJleHAiOjIzMTYyMzkwMjJ9.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"
    headers = {"Authorization": f"Bearer {bearer_token}", "Content-Type": "application/json"}
    payload = {"title": "Test Title", "body": "Test Body", "userId": 1}

    try:
      response = requests.post(url, headers=headers, json=payload)
      response.raise_for_status()
      print(f"Response status code: {response.status_code}")
      print(f"Response json: {response.json()}")
      assert response.status_code == 201
    except requests.exceptions.RequestException as e:
      print(f"An error occurred: {e}")



