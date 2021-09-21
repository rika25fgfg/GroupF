from django.urls import path
from . import views

app_name = 'nakano'
urlpatterns = [
    path('nakano', views.IndexView.as_view(), name="index"),
    
]
