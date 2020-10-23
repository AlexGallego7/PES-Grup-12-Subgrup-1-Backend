from django.conf.urls import url
from django.urls.conf import path

from . import views

urlpatterns = (
    url(r'^$', views.ReservationsView.as_view()),
    path('<id>', views.ReservationView.as_view()),
)
