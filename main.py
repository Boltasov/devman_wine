import datetime
import pandas

from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape


def years_ru(years_gap):
    last_digit = years_gap % 10
    if last_digit == 0 or (5 <= last_digit <= 9) or (11 <= years_gap % 100 <= 14):
        return 'лет'
    if 2 <= last_digit <= 4:
        return 'года'
    return 'год'


env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')

years_gap = datetime.datetime.now().year - 1920

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
