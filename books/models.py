from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Book(models.Model):
    CATEGORY_CHOICES = [
        ('Self Help', 'Self Help'),
        ('Fiction', 'Fiction'),
        ('Religious', 'Religious'),
        ('Programming', 'Programming'),
        ('Computer Science', 'Computer Science'),
    ]
    code = models.CharField(max_length=10, unique=True) 
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    year = models.IntegerField()
    copies = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='books/')

    def __str__(self):
        return self.title

class BorrowedBook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ['user', 'book']

    def __str__(self):
        return f"{self.user.username} - {self.book.title}"