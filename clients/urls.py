from django.conf.urls import url
from django.urls.conf import path

from . import views

urlpatterns = (
    url(r'^$', views.ClientsView.as_view()),
    url(r'^agenda', views.AgendaView.as_view()),
    path('<username>', views.ClientView.as_view()),


)
