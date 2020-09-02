from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('signup/', views.user_crete, name="signup"),
    path('login/', views.user_login, name="login"),
    path('logout/', views.user_logout, name="logout"),
    path('edit/', views.user_edit, name="edit"),
    path('list/', views.user_list, name="list"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)