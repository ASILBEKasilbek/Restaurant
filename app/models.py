from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='menu_images/', blank=True)

    def __str__(self):
        return self.name

class Galeriya(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='galeriya_images/', blank=True)

    def __str__(self):
        return str(self.id)