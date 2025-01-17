import pytest
from typing import Generator
from playwright.sync_api import Playwright, APIRequestContext


# @pytest.fixture(scope="session")
# def user_api_request_context(playwright: Playwright) -> Generator[APIRequestContext, None, None]:
#     request_context = playwright.request.new_context(
#         base_url="https://reqres.in"
#     )
#     yield request_context
#     request_context.dispose()

import requests

import requests
import pytest

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_todo_status_code():
    response = requests.get(f"{BASE_URL}/todos/1")
    assert response.status_code == 200

