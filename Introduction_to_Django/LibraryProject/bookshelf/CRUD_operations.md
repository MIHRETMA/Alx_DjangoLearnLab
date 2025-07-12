-----------create------------
# Open the Django shell
python manage.py shell

# Import the model
from bookshelf.models import Book

# Create the Book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

# Confirm creation
print(book)

# Expected Output:
# <Book: 1984>

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

