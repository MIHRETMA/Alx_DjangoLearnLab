# relationship_app/query_samples.py

import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library

def query_books_by_author(author_name):
    books = Author.objects.get(name=author_name)
    print(f"Books by {author_name}:")
    for book in books:
        print(f"- {book.title}")

def list_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        print(f"Books in {library.name}:")
        for book in library.books.all():
            print(f"- {book.title}")
    except Library.DoesNotExist:
        print(f"Library '{library_name}' not found.")

def get_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        print(f"Librarian for {library.name}: {library.librarian.name}")
    except Library.DoesNotExist:
        print(f"Library '{library_name}' not found.")
    except AttributeError:
        print(f"No librarian assigned to {library_name}.")

