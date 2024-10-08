from django.db import models

class Property(models.Model):
    title = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.PositiveIntegerField()  # tamanho em metros quadrados
    bedrooms = models.PositiveIntegerField()
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
