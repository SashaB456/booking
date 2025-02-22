from django.shortcuts import render
from rooms.models import Booking, Person, Room
# Create your views here.
def all_bookings(request):
    result = Booking.objects.all()
    context = {"bookings": result}
    return render(request, template_name = "templates/all_bookings.html", context=context)