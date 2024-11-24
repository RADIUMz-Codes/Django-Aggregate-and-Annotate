from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    book_name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6,decimal_places=2)
    publish_date = models.DateField()
    description = models.CharField(max_length=300, null=True, blank=True)

