from .views import RegisterAPI 
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterAPI


urlpatterns = [
    path('api/register/',RegisterAPI.as_view()),
    path("api/token/", TokenObtainPairView.as_view()),
    path("api/token/refresh/", TokenRefreshView.as_view()),
    path('api-auth/', include ('rest_framework.urls')),
]
