from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="home"),
    path('showorders/', views.showorders, name="showorders"),
    path('showorders/<int:id>/delete/', views.delete, name="delete"),
    path('showorders/<int:id>/update/', views.update, name="update"),
    path('showorders/<int:id>/update/updated/', views.updated, name="updated"),
    
    

    
]
