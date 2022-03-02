from django.db import models

# Create your models here.
class Address(models.Model):
    street = models.CharField(max_length=255)
    num = models.IntegerField()
    country = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.id}: {self.street} {self.num} {self.country}'


class Person(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.id}: {self.first_name} {self.last_name} ({self.email})'