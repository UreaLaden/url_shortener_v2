from django.urls import path,include
from . import views # The '.' means only within the current directory

urlpatterns = [
    path('',views.home),
    path('go',views.make_short_url),
    path('<str:short_url>',views.redirect_url)
]
