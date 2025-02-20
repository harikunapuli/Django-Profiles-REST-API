from django.urls import path # type: ignore
from profiles_api import views

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
]