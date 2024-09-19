from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    year = models.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2024)])
    rating = models.PositiveIntegerField(validators=[
        MaxValueValidator(10), MinValueValidator(1)])
    description = models.TextField(null=True, blank=True)

    posted_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    reviewTitle = models.CharField(max_length=100)
    review = models.CharField(max_length=300)
    posted_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.review
    

