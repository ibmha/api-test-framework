import requests
from config.base_config import BASE_URL

class APIClient:

    def get(self, endpoint):
        return requests.get(f"{BASE_URL}{endpoint}")

    def post(self, endpoint, payload):
        return requests.post(f"{BASE_URL}{endpoint}", json=payload)