from django.urls import path, include
from .views import UserCreateView, UserView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('users', UserView)

urlpatterns = [
    path('signup', UserCreateView.as_view()),
    path('', include (router.urls))
]