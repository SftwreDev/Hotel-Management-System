from django.urls import path

from .views import (
    homepage,
    create_reservations,
    reservations_list,
    delete_reservations,
    update_reservations,
    view_customers_reservation,
    reservations_list_view,
    update_reservations_view,

    room_list,
    delete_room,
    RoomUpdateView,

    check_in_and_out,
    list_of_check_in_or_out,
    delete_check_in,
    check_out,
    list_of_check_out
)

app_name = "reservations"

urlpatterns = [
    path("", homepage, name = 'homepage'),
    path("create-reservations", create_reservations, name = 'create_reservations'),
    path("list-of-reservations", reservations_list, name = 'reservations_list'),
    path("list-of-reservations-view/", reservations_list_view, name = 'reservations_list_view'),
    path("delete-reservations/<pk>/", delete_reservations, name = 'delete_reservations'),
    path("update-reservations/<pk>/", update_reservations, name = 'update_reservations'),
    path("update-reservations-view/<pk>/", update_reservations_view, name = 'update_reservations_view'),

    path("available-rooms/", room_list, name = 'room_list'),
    path("deleting-room/<pk>/", delete_room, name = 'delete_room'),
    path("update-room/<int:pk>/", RoomUpdateView.as_view(), name = 'update_room'),

    path("customer-reservation-rooms/", view_customers_reservation, name = 'view_customers_reservation'),
    path("check-in-or-out/<int:pk>/", check_in_and_out, name = 'check_in_and_out'),
    path("list-of-check-in-customers/", list_of_check_in_or_out, name = 'list_of_check_in_or_out'),
    path("delete-checked-in-customer/<int:pk>/", delete_check_in, name = 'delete_check_in'),
    path("check-out/<pk>/", check_out, name = 'check_out'),
    path("checked-out-list/", list_of_check_out, name = 'list_of_check_out'),

    
]