# Open the Django shell
python manage.py shell

# Import the model
from bookshelf.models import Book

# Retrieve the book titled "1984"
book = Book.objects.get(title="1984")

# Display all attributes of the book
print(book.title)
print(book.author)
print(book.publication_year)

# Expected Output:
# 1984 
# George Orwell 
# 1949

