-----------delete---------------
# Open the Django shell
python manage.py shell

# Import the model
from bookshelf.models import Book

#Delete Book instance
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

Book.objects.all()

# Expected Output:
# <QuerySet []>

