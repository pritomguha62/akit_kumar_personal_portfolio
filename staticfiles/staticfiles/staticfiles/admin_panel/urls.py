
from django.contrib import admin
from django.urls import path, include
from admin_panel import views
from middlewares.admin_auth import admin_middleware

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('service/', include("service.urls")),
    path('', views.dashboard),
    path('dashboard/', admin_middleware(views.dashboard), name='dashboard'),
    path('signin/', views.signin, name='admin_panel.signin'),
    path('signup/', views.signup, name='admin_panel.signup'),
    path('signin_info/', views.signin_info, name='admin_panel.signin_info'),
    path('signup_info/', views.signup_info, name='admin_panel.signup_info'),
    path('sign_out/', views.sign_out, name='admin_panel.sign_out'),
]