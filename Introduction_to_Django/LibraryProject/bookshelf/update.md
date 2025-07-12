-----------update---------------
# Open the Django shell
python manage.py shell

# Import the model
from bookshelf.models import Book

#Update Book instance
book = Book.objects.get(title="1984")

book.title = "1984 new"
book.save()

print(book.title)

# Expected Output:
# 1984 new
