# pylint: disable=invalid-name
import requests


class AppLibrary:
    def __init__(self):
        self._base_url = "http://localhost:5001"

    def reset_application(self):
        requests.post(f"{self._base_url}/tests/reset", timeout=1)

    def create_user(self, username, password):
        data = {
            "username": username,
            "password": password,
            "password_confirmation": password,
        }

        requests.post(f"{self._base_url}/register", data=data, timeout=1)
