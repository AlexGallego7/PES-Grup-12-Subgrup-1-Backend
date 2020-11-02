from django.conf.urls import url
from django.urls.conf import path

from . import views

urlpatterns = (
    url(r'^$', views.ManagersView.as_view()),
    path('<username>', views.ManagerView.as_view()),
)
