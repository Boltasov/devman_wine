import datetime
import os

import pandas

from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape


FOUNDATION_YEAR = 1920


def years_ru(years_gap):
    last_digit = years_gap % 10
    if last_digit == 0 or (5 <= last_digit <= 9) or (11 <= years_gap % 100 <= 14):
        return 'лет'
    if 2 <= last_digit <= 4:
        return 'года'
    return 'год'


def get_products(file_path):
    products = {}
    products_df = pandas.read_excel(file_path, na_values='nan', keep_default_na=False)
    products_df.columns = ['category', 'name', 'kind', 'price', 'image', 'sale']
    categories = set(products_df['category'])
    for category in categories:
        products[category] = products_df.loc[products_df['category'] == category].to_dict('records')

    return products


if __name__ == '__main__':
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')

    years_gap = datetime.datetime.now().year - FOUNDATION_YEAR

    file_path = os.getenv('FILE_PATH', default='wine.xlsx')
    products = get_products(file_path)

    rendered_page = template.render(
        categories=products,
        age=f'{str(years_gap)} {years_ru(years_gap)}',
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()
