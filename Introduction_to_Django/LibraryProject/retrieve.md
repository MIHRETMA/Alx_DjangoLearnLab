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

