"""talentoHumano URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from convocatorias.views import after_login
from graphene_django.views import GraphQLView

urlpatterns = [
    path('', include('convocatorias.urls'), name='convocatorias'),
    path('aspirante/', include('aspirante.urls'), name='aspirante'),
    path('empresa/', include('empresa.urls'), name='empresa'),
    path('admin/', admin.site.urls),

    # Rutas de autenticación
    path('login', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('after_login', after_login, name='afterLogin'),
    path('logout', auth_views.logout_then_login, name='logout'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='auth/password_reset_form.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='auth/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='auth/password_reset_complete.html'), name='password_reset_complete'),

    # Ruta API
    path('api/', include('apiEmpresa.urls'), name='apiEmpresa'),
]
