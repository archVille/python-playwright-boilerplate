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