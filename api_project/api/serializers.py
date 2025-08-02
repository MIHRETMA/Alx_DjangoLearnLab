from rest_framework import serializers
from .models import Book  # Adjust the import path based on your project structure

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'  # Includes all fields from the Book model
