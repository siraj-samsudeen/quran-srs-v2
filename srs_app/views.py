from django.shortcuts import redirect, render
from .models import Student


def home(request):
    return redirect("student_list")


def student_list(request):
    if request.POST:
        Student.objects.create(name=request.POST["student-name"])
        return redirect("student_list")

    students = Student.objects.all()

    return render(request, "student_list.html", {"students": students})
