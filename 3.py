"""
Объединение данных из разных источников
Напишите скрипт на Python, который объединяет данные
из двух источников. Первый источник - это CSV-файл
с информацией о продуктах (поля: product_id, product_name).
Второй источник - это JSON-файл с данными о продажах
(поля: sale_id, product_id, amount).
Скрипт должен объединить данные по product_id и
вывести итоговую таблицу с информацией о продажах для каждого продукта.
"""
import pandas as pd

products = pd.read_csv('products.csv', sep=';')
sales = pd.read_json('sales.json')
result = pd.merge(products, sales, on='product_id').set_index('product_id')
result.to_csv('3_result.csv')
