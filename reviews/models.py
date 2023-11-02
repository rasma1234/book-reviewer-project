from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    review_text = models.TextField()
    rating = models.IntegerField(choices= [(1, '1'),(2, '2'),(3, '3'),(4, '4'),(5, '5')])

    
    
