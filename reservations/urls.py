from django.urls import path

from .views import (
    homepage,
    create_reservations,
    reservations_list,
    delete_reservations,
    update_reservations,

    room_list,
    delete_room
)

app_name = "reservations"

urlpatterns = [
    path("", homepage, name = 'homepage'),
    path("create-reservations", create_reservations, name = 'create_reservations'),
    path("list-of-reservations", reservations_list, name = 'reservations_list'),
    path("delete-reservations/<pk>/", delete_reservations, name = 'delete_reservations'),
    path("update-reservations/<pk>/", update_reservations, name = 'update_reservations'),

    path("available-rooms/", room_list, name = 'room_list'),
    path("deleting-room/<pk>/", delete_room, name = 'delete_room'),
]
