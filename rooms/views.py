from django.shortcuts import render, HttpResponse, redirect
from rooms.models import Booking, Person, Room
# Create your views here.
def all_bookings(request):
    result = Booking.objects.all()
    context = {"bookings": result}
    return render(request, template_name = "all_bookings.html", context=context)
def create_booking(request):
    if request.method == "POST":
        start_date = request.POST.get("start_date", default="2025-02-28 16:37")
        end_date = request.POST.get("end_date", default="2025-04-10 18:29")
        room_num = request.POST.get("room_id", default=1)
        user1 = request.POST.get("user_id", default=1)
        try:
            room1 = Room.objects.get(number=room_num)
            person1 = Person.objects.get(username=user1)
        except ValueError:
            return HttpResponse("Error", status=400)
        except Room.DoesNotExist:
            return HttpResponse("Not found", status=404)
        booking = Booking.objects.create(
            person=person1,
            available=True,
            start_date=start_date,
            end_date=end_date,
            room = room1
        )
        return redirect("all-bookings")
    else:
        return render(request, template_name="create_booking.html")
def get_all_users(request):
    result = Person.objects.all()
    context = {'people': result}
    return render(request, template_name='all_users.html', context=context)
def delete_booking(request, HttpResponse):
    if request.method == "POST":
        id_booking = request.POST.get("deleted-id", default=1)
        try:
            deleted_booking = Booking.objects.get(id=id_booking)
        except ValueError:
            return HttpResponse("Invalid value", status=400)
        except Booking.DoesNotExist:
            return HttpResponse("Not found", status=404)
        Booking.objects.delete(id=id_booking)
        return redirect('all-bookings')
    else:
        return render(request, template_name='delete_booking.html')