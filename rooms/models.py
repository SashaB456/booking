from django.db import models

# Create your models here.
class Booking(models.Model):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    available = models.BooleanField()
    person = models.ForeignKey("Person", on_delete=models.CASCADE)
    room = models.ForeignKey("Room", on_delete=models.CASCADE)
    class Meta:
        verbose_name = "Booking"
        verbose_name_plural = "Bookings"
    def __str__(self):
        return f"{self.start_date}"
class Room(models.Model):
    number = models.IntegerField(default=1)
    capacity = models.IntegerField()
    rating = models.FloatField()
    class Meta:
        verbose_name = "Room"
        verbose_name_plural = "Rooms"
    def __str__(self):
        return f"{self.number}"
class Person(models.Model):
    username = models.CharField(max_length=100, default="Kamel")
    email = models.EmailField()

    class Meta:
        verbose_name = "Person"
        verbose_name_plural = "People"
    def __str__(self):
        return f"{self.username}"