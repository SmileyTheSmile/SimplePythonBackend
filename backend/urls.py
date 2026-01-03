from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

from project import views
from django.views.generic import RedirectView
from django.contrib.auth.views import (
    LogoutView,
    PasswordResetView,
)

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"groups", views.GroupViewSet)

urlpatterns = [
     path('',
          RedirectView.as_view(pattern_name='login', permanent=False),
          name='index'),
     path('admin/',
          admin.site.urls,
          name='admin'),
     path('login/',
          views.LoginView.as_view(),
          name='login'),
     path('logout/',
          LogoutView.as_view(next_page='login'),
          name='logout'),
     path('signup/',
          views.SignUpView.as_view(),
          name='signup'),
     path('profile/<int:pk>/',
          views.ProfileView.as_view(),
          name='profile'),
     path('settings/',
          views.ProfileSettingsView.as_view(),
          name='profile_settings'),
     path('password_reset/',
          PasswordResetView.as_view(),
          name='password_reset'),
    #  path("", include(router.urls)),
    #  path("api/auth/", 
    #       include("rest_framework.urls", namespace="rest_framework")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)