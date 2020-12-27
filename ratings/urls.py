from django.conf.urls import url
from django.urls.conf import path

from . import views

urlpatterns = (
    url(r'^$', views.RatingsView.as_view()),
    path('<id>', views.RatingView.as_view()),
)
