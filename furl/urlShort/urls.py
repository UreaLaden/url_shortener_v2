from django.urls import path,include
from . import views # The '.' means only within the current directory

urlpatterns = [
    path('',views.home)
]
