from django.urls import path
import rooms.views as room_views
urlpatterns = [path("", room_views.all_bookings, name="all_bookings"),]