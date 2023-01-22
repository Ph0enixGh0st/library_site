from http.server import HTTPServer, SimpleHTTPRequestHandler
from more_itertools import chunked
from livereload import Server, shell
from jinja2 import Environment, FileSystemLoader, select_autoescape
import json, urllib
from pathlib import Path


def on_reload(template):
    with open('books_about.json', 'r', encoding="utf8") as json_file:
        books = json.load(json_file)

    books_per_page = 10
    chunked_books = list(chunked(books, books_per_page))
    chunked_book_per_page = 1
    chunked_pages = list(chunked(chunked_books, chunked_book_per_page))
    pages_path = Path('pages')
    pages_path.mkdir(parents=True, exist_ok=True)
    
    for page_num, books in enumerate(chunked_pages, 1):
        rendered_page = template.render(
            books_per_page=books,
            pages_count=len(chunked_books),
            current_page=page_num,
        )
        with open(pages_path / f'index{page_num}.html', 'w', encoding="utf-8") as file:
            file.write(rendered_page)


        #rendered_page = template.render(
                #books=books,
            #)

        #with open('index.html', 'w', encoding="utf-8") as file:
            #file.write(rendered_page)


def main():
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')
    on_reload(template)

    server = Server()
    server.watch('template.html', on_reload(template))
    server.serve(root='.', default_filename='pages/index1.html')


if __name__ == '__main__':
    main()