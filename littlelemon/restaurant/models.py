from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator

# Booking Model
class Booking(models.Model):
    name = models.CharField(max_length=255)  # changed to snake_case
    booking_date = models.DateField(default=timezone.now)  # changed to snake_case
    no_of_guests = models.SmallIntegerField(default=10, validators=[MinValueValidator(1)])  # added validator for guests

    def __str__(self):
        return f'{self.name}: {self.booking_date}'  # changed to snake_case


# Menu Model
class Menu(models.Model):
    title = models.CharField(max_length=255)  # changed to snake_case
    price = models.DecimalField(max_digits=10, decimal_places=2)  # changed to snake_case
    inventory = models.IntegerField(default=5, validators=[MinValueValidator(0)])  # added validator for inventory

    def __str__(self):
        return f'{self.title}: ${self.price:.2f}'  # changed to snake_case
