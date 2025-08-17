-----------update---------------
# Open the Django shell
python manage.py shell

# Import the model
from bookshelf.models import Book

#Update Book instance
book = Book.objects.get(title="1984")

book.title = "Nineteen Eighty-Four"
book.save()

print(book.title)

# Expected Output:
# Nineteen Eighty-Four
