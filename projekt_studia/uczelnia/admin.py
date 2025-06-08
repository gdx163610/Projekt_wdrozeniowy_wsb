from django.contrib import admin
from .models import Student, Lecturer, Subject, Group, Grade, Schedule, News


admin.site.register(Student)
admin.site.register(Lecturer)
admin.site.register(Subject)
admin.site.register(Group)
admin.site.register(Grade)

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('student', 'subject', 'lecturer', 'date', 'start_time', 'end_time', 'location')
    list_filter = ('date', 'lecturer', 'location')  # Dodanie filtrów
    search_fields = ('student__first_name', 'student__last_name', 'subject__name')  # Dodanie pola wyszukiwania

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'created_by')
    search_fields = ('title', 'content')
    list_filter = ('created_at',)
