from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from certificates import views as cert_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', cert_views.home, name='home'),
    path('certificate_expiry/', cert_views.certificate_expiry_list, name='certificate_expiry_list'),
    path('certificate_user/', cert_views.certificate_user_list, name='certificate_user_list'),
    path('login/', auth_views.LoginView.as_view(template_name='certificates/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
]
