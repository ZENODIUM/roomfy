from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('<str:username>/edit/', views.edit_profile, name='edit_profile'),
    path('<str:username>/', views.view_profile, name='profile'),
]
if settings.DEBUG:  # Serve media files during development only
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)