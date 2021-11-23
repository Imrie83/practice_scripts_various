from django.db import models


class User(models.Model):
    name = models.CharField(max_length=32, null=True)
    surname = models.CharField(max_length=32, null=True)

    def __str__(self):
        return f'{self.name} {self.surname}'


class Post(models.Model):
    content = models.TextField()
    date_added = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.author} - {self.date_added}'