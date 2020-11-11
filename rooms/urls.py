from django.conf.urls import url
from django.urls.conf import path

from . import views

urlpatterns = (
    url(r'^$', views.RoomsView.as_view()),
    path('<id>', views.RoomView.as_view()),
)