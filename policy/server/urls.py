from django.urls import path
from . import views

urlpatterns = [
    path("service/configuration", views.service_configuration, name="service"),
    path("participant/location", views.participant_location, name="location"),
    path("participant/avatar", views.participant_avatar, name="avatar"),
    path("registrations", views.registrations, name="registrations"),
]
