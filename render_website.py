from http.server import HTTPServer, SimpleHTTPRequestHandler
from more_itertools import chunked
from livereload import Server, shell
from jinja2 import Environment, FileSystemLoader, select_autoescape
import json, urllib
from pathlib import Path


def on_reload(template):
    with open('books_about.json', 'r', encoding="utf8") as json_file:
        books = json.load(json_file)

        rendered_page = template.render(
                books=books,
            )

        with open('index.html', 'w', encoding="utf-8") as file:
            file.write(rendered_page)


def main():
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')
    on_reload(template)

    server = Server()
    server.watch('template.html', on_reload(template))
    server.serve(root='.')


if __name__ == '__main__':
    main()