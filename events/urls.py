from django.conf.urls import url
from django.urls.conf import path

from . import views

urlpatterns = (
    url(r'^$', views.EventsView.as_view()),
    path('<name>', views.EventView.as_view()),
)
