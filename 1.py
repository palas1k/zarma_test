"""

1. Подключение к API и получение данных
Напишите скрипт на Python, который подключается к API
и получает данные. Например, используйте публичное API
https://jsonplaceholder.typicode.com/posts.
Сохраните полученные данные в формате JSON в файл.
"""

import requests


class PostHandlers:
    def __init__(self, url: str):
        self.url = url

    @staticmethod
    def _save_in_json(post: str) -> None:
        with open('1_response.json', 'w') as file:
            file.write(post)

    def save_posts(self):
        response = requests.get(self.url)
        return self._save_in_json(response.text)


post = PostHandlers('https://jsonplaceholder.typicode.com/posts/')
post.save_posts()
