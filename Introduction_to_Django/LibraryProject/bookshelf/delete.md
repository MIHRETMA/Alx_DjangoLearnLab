-----------delete---------------
# Open the Django shell
python manage.py shell

# Import the model
from bookshelf.models import Book

#Delete Book instance
book = Book.objects.get(title="1984 new")
book.delete()

Book.objects.all()

# Expected Output:
# <QuerySet []>

