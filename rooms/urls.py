from django.urls import path
import rooms.views as room_views
urlpatterns = [path("", room_views.all_bookings, name="all-bookings"),path("create-booking/", room_views.post_dates, name="create-booking"),]