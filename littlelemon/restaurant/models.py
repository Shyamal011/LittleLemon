from django.db import models
from django.utils import timezone

# Create your models here.
class Booking(models.Model):
    Name = models.CharField(max_length=255)
    BookingDate = models.DateField(default=timezone.now)
    No_of_guests = models.SmallIntegerField(default=10)

    def __str__(self):
        return f'{self.Name}: {self.BookingDate}'
    
class Menu(models.Model):
    Title = models.CharField(max_length=255)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Inventory = models.IntegerField(default=5)

    def __str__(self):
        return f'{self.Title}: ${self.Price:.2f}'