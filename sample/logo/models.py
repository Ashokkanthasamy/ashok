from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    city = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name
