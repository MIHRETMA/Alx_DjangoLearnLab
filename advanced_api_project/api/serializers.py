from rest_framework import serializers
from .models import Book, Author


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'  #for serializing all fields

    def validate_publication_year(self, value): #function for validating publication year
        current_year = datetime.now().year  #defining current_year using datetime module
        if value > current_year:
            raise serializers.ValidationError("Publication cannot be in future")    #error to raise if publication year is greater than current_year
        return value


class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)   #nesting BookSerializer

    class Meta:
        model = Author
        fields = ['name','books']   #serializing only name field
