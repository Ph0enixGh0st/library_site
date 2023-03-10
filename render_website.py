import argparse
import json
import os
import urllib
from pathlib import Path

from dotenv import load_dotenv
from jinja2 import Environment, FileSystemLoader, select_autoescape
from livereload import Server
from more_itertools import chunked


def insert_path(on_reload):
    load_dotenv()
    books_repository = os.environ.setdefault('BOOKS_REPOSITORY', 'media/books_about.json')
    def wrapped():
        return on_reload(books_repository)
    return wrapped


@insert_path
def on_reload(books_repository):

    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
        )
    template = env.get_template('template.html')

    with open(books_repository, 'r', encoding='utf8') as json_file:
        books_descriptions = json.load(json_file)

    books_per_page = 10
    chunked_books = list(chunked(books_descriptions, books_per_page))

    chunked_books_per_page = 1
    chunked_pages = list(chunked(chunked_books, chunked_books_per_page))

    pages_path = Path('pages')
    pages_path.mkdir(parents=True, exist_ok=True)

    for page_num, books in enumerate(chunked_pages, 1):
        rendered_page = template.render(
            books_per_page=books,
            pages_count=len(chunked_books),
            current_page=page_num
        )
        with open(f'{pages_path}/index{page_num}.html', 'w', encoding='utf-8') as html_file:
            html_file.write(rendered_page)


def main():

    on_reload()

    server = Server()
    server.watch('template.html', on_reload)
    server.serve(root='.', default_filename='pages/index1.html')


if __name__ == '__main__':
    main()