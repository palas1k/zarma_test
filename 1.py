"""

1. Подключение к API и получение данных
Напишите скрипт на Python, который подключается к API
и получает данные. Например, используйте публичное API
https://jsonplaceholder.typicode.com/posts.
Сохраните полученные данные в формате JSON в файл.
"""
import json

import requests
from requests import Response


class PostRequest:
    @staticmethod
    def get_response(url: str, request_manager=requests) -> Response:
        try:
            response = request_manager.get(url)
            return response
        except Exception as e:
            raise e


class PostSave:

    @staticmethod
    def _get_data(url: str) -> json:
        post_request = PostRequest()
        resp = post_request.get_response(url)
        return resp.text

    def get_by_url_and_save_in_json(self, url) -> None:
        data = self._get_data(url)
        with open('1_response.json', 'w') as file:
            file.write(data)


post_save = PostSave()
post_save.get_by_url_and_save_in_json('https://jsonplaceholder.typicode.com/posts')
