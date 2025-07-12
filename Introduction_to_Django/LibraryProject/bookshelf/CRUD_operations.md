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

-----------retrieve---------------
# Open the Django shell
python manage.py shell

# Import the model
from bookshelf.models import Book

#Retrieve Book instance
books = Book.objects.all()

for i in books:
	print(i.title, i.author, i.publication_year)

# Expected Output:
# 1984 George Orwell 1949



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
