from django.urls import path
import rooms.views as room_views
urlpatterns = [path("all-bookings/", room_views.all_bookings, name="all-bookings"),
               path("create-booking/", room_views.create_booking, name="create-booking"),
               path("all-users/", room_views.get_all_users, name="all-users"),
               path("delete-booking/", room_views.delete_booking, name="delete-booking"),]