import datetime
import pandas
import pprint

from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
from collections import defaultdict


def years_ru(years_gap):
    last_digit = years_gap % 10
    if last_digit == 0 or (5 <= last_digit <= 9) or (11 <= years_gap % 100 <= 14):
        return 'лет'
    if 2 <= last_digit <= 4:
        return 'года'
    return 'год'


def get_products(file):
    products = {}
    products_df = pandas.read_excel(file, na_values='nan', keep_default_na=False)
    categories = set(products_df['Категория'])
    for category in categories:
        products[category] = products_df.loc[products_df['Категория'] == category].to_dict('records')

    return products


if __name__ == '__main__':
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')

    years_gap = datetime.datetime.now().year - 1920

    file = 'wine2.xlsx'
    products = get_products(file)

    wines = pandas.read_excel('wine.xlsx')
    wines.columns = ['name', 'kind', 'price', 'image']

    rendered_page = template.render(
        wines=wines.to_dict('records'),
        age=f'{str(years_gap)} {years_ru(years_gap)}',
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()

'''
pprint.pprint(products)'''
