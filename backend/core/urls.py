from django.urls import include, path

from . import views

urlpatterns = [
    path("api/hello/", views.index.as_view(), name="index"),
]
