from django.shortcuts import render
from .models import Student


def home_page(request):
    # If it is get, student_name will be null
    if request.POST:
        Student.objects.create(name=request.POST['student-name'])

    students = Student.objects.all()

    return render(request, "home.html",
                  {'students': students})
