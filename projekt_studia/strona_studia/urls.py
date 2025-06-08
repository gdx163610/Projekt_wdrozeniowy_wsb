from django.contrib import admin
from django.urls import path, include  # Upewnij się, że "include" zostało zaimportowane
from uczelnia import views  # Importowanie widoków z aplikacji "uczelnia"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('uczelnia.urls')),  # Łączenie URL-i aplikacji "uczelnia"

]
