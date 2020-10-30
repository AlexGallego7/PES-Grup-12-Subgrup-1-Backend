from django.conf.urls import url
from django.urls.conf import path

from . import views

urlpatterns = (
    url(r'^$', views.MeasuresView.as_view()),
    path('<name>', views.MeasureView.as_view()),
)
