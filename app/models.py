from django.db import models


class Book(models.Model):
    author = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    isbn = models.PositiveBigIntegerField()

    def __str__(self):
        return self.title


class Opinion(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='opinions')
    rate = models.PositiveSmallIntegerField()
    description = models.TextField()
    isbn = models.PositiveBigIntegerField()

    def __str__(self):
        return f'({str(self.book)}) {self.description}'
