import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        response.raise_for_status()
        return response.content

    def load_json(self):
        body_bytes = self.get_response_body()
        body_str = body_bytes.decode('utf-8')
        return json.loads(body_str)