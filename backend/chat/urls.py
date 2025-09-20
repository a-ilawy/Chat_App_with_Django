from django.urls import path
from . import views

urlpatterns = [
    path("", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("chat/", views.HomeView, name="chat"),
    path("<str:room_name>/<str:username>/", views.RoomView, name="room")
]