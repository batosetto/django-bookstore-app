from django.forms import ModelForm
from. models import Book, Review

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        exclude = ["posted_by"]

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
        exclude = ["posted_by"]
        

