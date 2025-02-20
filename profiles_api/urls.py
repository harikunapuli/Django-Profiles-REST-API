from django.urls import path, include # type: ignore
from rest_framework.routers import DefaultRouter # type: ignore
from profiles_api import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename='hello-viewset')
urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('', include(router.urls)),
]