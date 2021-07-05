from django.test import TestCase
from django.urls import resolve
from pytest_django.asserts import assertContains, assertTemplateUsed
import pytest

from .views import home_page
from .models import Student


def describe_home_page():
    def template_is_available(client, db):
        assertTemplateUsed(client.get("/"), 'home.html')


@pytest.mark.django_db
def describe_manage_students():
    def add_one_student(client):
        response = client.post("/", {'student-name': 'dummy_student1'})
        assertContains(response, "dummy_student1")
        assertTemplateUsed(response, "home.html")
        assert Student.objects.count() == 1

        # TODO Redirect after Post

    def add_two_students(client):
        response = client.post("/", {'student-name': 'dummy_student1'})
        response = client.post("/", {'student-name': 'dummy_student2'})
        assertContains(response, "dummy_student1")
        assertContains(response, "dummy_student2")

        assert Student.objects.count() == 2


def describe_student_model():
    def add_students(db):
        student1 = Student.objects.create(name="dummy_student1")
        assert Student.objects.count() == 1

        student2 = Student.objects.create(name="dummy_student2")
        assert Student.objects.count() == 2

        students = Student.objects.all()
        assert student1 in students
        assert student2 in students
