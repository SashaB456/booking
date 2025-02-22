from django.contrib import admin

# Register your models here.
from rooms.models import Booking, Person, Room
admin.site.register(Booking)
admin.site.register(Person)
admin.site.register(Room)