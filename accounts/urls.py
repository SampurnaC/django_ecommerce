from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import SigninForm

app_name = 'accounts'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html', authentication_form=SigninForm), name='login'),
    path('logout/', views.logout_user, name='logout'),

]
