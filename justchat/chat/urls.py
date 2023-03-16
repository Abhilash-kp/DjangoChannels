# chat/urls.py
from django.urls import path

from . import views
from .views import SignUp

app_name = 'chat'

urlpatterns = [
    path("", views.room, name="room"),
    path('report/', views.generate_report, name="report"),
    # path("<str:room_name>/", views.room, name="room"),

]