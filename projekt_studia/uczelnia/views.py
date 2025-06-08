from django.shortcuts import render, get_object_or_404, redirect # type: ignore
from django.contrib.auth import authenticate, login, logout # type: ignore
from django.contrib.auth.decorators import login_required # type: ignore
from django.utils.dateparse import parse_date # type: ignore
from django.http import HttpResponseBadRequest, JsonResponse # type: ignore
from django.utils import timezone
from datetime import datetime
from django.views.decorators.http import require_POST
from .models import Student, Lecturer, Subject, Group, Grade, Schedule, News, NewsRead
from django.db.models import Q

# Strona startowa (logowanie)
def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Przekierowanie na stronę główną
        else:
            return render(request, 'uczelnia/login.html', {'error': 'Nieprawidłowa nazwa użytkownika lub hasło'})
    return render(request, 'uczelnia/login.html')

# Wylogowanie
def logout_view(request):
    logout(request)
    return redirect('login')

# Widok strony głównej (chroniony logowaniem)
@login_required
def home(request):
    user = request.user

    if hasattr(user, 'student'):
        upcoming_lessons = (
            Schedule.objects
            .filter(student=user.student, date__gte=timezone.localdate())
            .order_by('date', 'start_time')[:5]
        )
        recent_grades = (
            Grade.objects
            .filter(student=user.student)
            .order_by('-date')[:5]
        )
    else:
        upcoming_lessons = []
        recent_grades = []

    unread_notifications = 0
    news_count = News.objects.exclude(newsread__user=request.user).count()

    return render(request, 'uczelnia/home.html', {
        'user': user,
        'upcoming_lessons': upcoming_lessons,
        'recent_grades': recent_grades,
        'unread_notifications': unread_notifications,
        'news_count': news_count,
    })

# Widok listy studentów (chroniony logowaniem)
@login_required
def student_list(request):
    query = request.GET.get('search', '')  # Pobierz wartość parametru 'search' z URL
    if query:
        students = Student.objects.filter(
            first_name__icontains=query  # Szukaj w polu 'first_name'
        ) | Student.objects.filter(
            last_name__icontains=query   # Szukaj w polu 'last_name'
        ) | Student.objects.filter(
            email__icontains=query       # Szukaj w polu 'email'
        )
    else:
        students = Student.objects.all()  # Jeśli brak zapytania, pokaż wszystkich studentów

    return render(request, 'uczelnia/student_list.html', {'students': students, 'query': query})

# Widok szczegółowy dla jednego studenta (chroniony logowaniem)
@login_required
def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    grades = Grade.objects.filter(student=student)
    return render(request, 'uczelnia/student_detail.html', {'student': student, 'grades': grades})

# Widok listy wykładowców (chroniony logowaniem)
@login_required
def lecturer_list(request):
    query = request.GET.get('search', '')  # Pobierz wartość parametru 'search' z URL
    lecturers = Lecturer.objects.all()  # Jeśli brak zapytania, pokaż wszystkich wykładowców
    if query:
        lecturers = lecturers.filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(subject__name__icontains=query)
        ).distinct()

    return render(request, 'uczelnia/lecturer_list.html', {'lecturers': lecturers, 'query': query})

# Widok szczegółowy dla jednego wykładowcy (chroniony logowaniem)
@login_required
def lecturer_detail(request, pk):
    lecturer = get_object_or_404(Lecturer, pk=pk)
    subjects = Subject.objects.filter(lecturer=lecturer)
    return render(request, 'uczelnia/lecturer_detail.html', {'lecturer': lecturer, 'subjects': subjects})

# Widok listy przedmiotów (chroniony logowaniem)
@login_required
def subject_list(request):
    subjects = Subject.objects.all()
    return render(request, 'uczelnia/subject_list.html', {'subjects': subjects})

@login_required
def user_profile_view(request):
    return render(request, 'user_profile.html', {'user': request.user})

# Widok terminarza zajęć (chroniony logowaniem)
@login_required
def student_schedule(request):
    date_str = request.GET.get('date')
    if date_str:
        selected_date = datetime.strptime(date_str, "%Y-%m-%d").date()
    else:
        selected_date = timezone.localdate()  # dzisiejsza data

    schedule = Schedule.objects.filter(student=request.user.student, date=selected_date)
    return render(request, 'uczelnia/student_schedule.html', {
        'schedule': schedule,
        'selected_date': selected_date,
    })

@login_required
def grades_view(request):
    # Jeśli student, pokazuj tylko jego oceny
    if hasattr(request.user, 'student'):
        grades = Grade.objects.filter(student=request.user.student)
    else:
        # Jeśli wykładowca/admin, pokazuj wszystkie oceny
        grades = Grade.objects.all()
    return render(request, 'uczelnia/grades.html', {'grades': grades})

@login_required
def news_json(request):
    news = News.objects.order_by('-created_at')[:10]
    read_ids = set(NewsRead.objects.filter(user=request.user, news__in=news).values_list('news_id', flat=True))
    data = [
        {
            'id': n.id,
            'title': n.title,
            'content': n.content,
            'created_at': n.created_at.strftime('%d.%m.%Y %H:%M'),
            'read': n.id in read_ids
        }
        for n in news
    ]
    return JsonResponse({'news': data})

@require_POST
@login_required
def mark_news_read(request):
    news_id = request.POST.get('news_id')
    if news_id:
        news = News.objects.filter(id=news_id).first()
        if news:
            NewsRead.objects.get_or_create(user=request.user, news=news)
            return JsonResponse({'status': 'ok'})
    return JsonResponse({'status': 'error'}, status=400)