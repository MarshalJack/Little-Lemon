from django.db import models

# # Create your models here.
class Menu(models.Model):
    id=models.IntegerField(primary_key=True)
    title=models.CharField(max_length=255)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    inventory=models.SmallIntegerField()

class Booking(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=255)
    no_of_guests=models.SmallIntegerField()
    booking_date=models.DateField()