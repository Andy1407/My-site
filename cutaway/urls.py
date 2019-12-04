from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'cutaway'
urlpatterns = [
    path('', views.basic, name='basic'),
    path('add/', views.add, name='add'),
] + static(settings.MEDIA_URL,  document_root=settings.MEDIA_ROOT)
