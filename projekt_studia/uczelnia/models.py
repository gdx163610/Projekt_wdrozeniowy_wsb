from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Model reprezentujący studentów
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    enrollment_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} ({self.first_name} {self.last_name})"

# Model reprezentujący wykładowców
class Lecturer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Model reprezentujący przedmioty
class Subject(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# Model reprezentujący grupy studentów
class Group(models.Model):
    name = models.CharField(max_length=50)
    year = models.IntegerField()

    def __str__(self):
        return self.name

# Model reprezentujący oceny
class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    grade = models.DecimalField(max_digits=4, decimal_places=2)  # np. 4.5
    date = models.DateField()

    def __str__(self):
        return f"{self.student} - {self.subject} - {self.grade}"

# Model reprezentujący terminarz zajęć
class Schedule(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE)
    lecturer = models.ForeignKey('Lecturer', on_delete=models.SET_NULL, null=True)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.subject.name} ({self.date})"

# Model reprezentujący wiadomości
class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

# Model reprezentujący przeczytane wiadomości
class NewsRead(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    news = models.ForeignKey('News', on_delete=models.CASCADE)
    read_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'news')
