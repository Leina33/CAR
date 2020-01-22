from django.db import models

# Create your models here.
class CarMake(models.Model):
    picture = models.FileField(null=True)
    brand = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    car_make = models.CharField(max_length=100, null=True)
    price = models.IntegerField(null=True)
    fuel = models.CharField(max_length=20, null=True)
    dimensions = models.CharField(max_length=50, null=True)
    transmission = models.CharField(max_length=100, null=True)
    gears = models.IntegerField(null=True)
    seats = models.IntegerField(null=True)
    power = models.IntegerField(null=True)
    tank_capacity = models.IntegerField(null=True)
    engine_displacement = models.IntegerField(null=True)
    # added_by = models.ForeignKey(User, on_delete=None, null=True)
    description = models.TextField()

    def __str__(self):
        return self.brand + " " + self.name



class Order(models.Model):
    car_make=models.ForeignKey(CarMake, on_delete=models.CASCADE)
    amount=models.IntegerField()
    order_time = models.DateTimeField(auto_now_add=True)
    
    


        