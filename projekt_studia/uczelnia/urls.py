from django.contrib import admin
from django.urls import path, include
from uczelnia import views  # Import widoków z aplikacji "uczelnia"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_view, name='login'),  # Strona logowania
    path('home/', views.home, name='home'),  # Strona główna po zalogowaniu
    path('students/', views.student_list, name='student_list'),  # Lista studentów
    path('schedule/', views.student_schedule, name='student_schedule'),  # Terminarz zajęć
    path('students/<int:pk>/', views.student_detail, name='student_detail'),  # Szczegóły studenta
    path('lecturers/', views.lecturer_list, name='lecturer_list'),  # Lista wykładowców
    path('lecturers/<int:pk>/', views.lecturer_detail, name='lecturer_detail'),  # Szczegóły wykładowcy
    path('subjects/', views.subject_list, name='subject_list'),  # Lista przedmiotów
    path('logout/', views.logout_view, name='logout'), # wylogowanie
    path('user_profile/', views.user_profile_view, name='user_profile'),# Wyszukiwanie wykładowców
    path('grades/', views.grades_view, name='grades'),  # Widok ocen
    path('news_json/', views.news_json, name='news_json'),
    path('mark_news_read/', views.mark_news_read, name='mark_news_read'),
]

