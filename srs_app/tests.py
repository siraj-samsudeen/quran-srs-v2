from django.test import TestCase
from django.urls import resolve
from django.urls.base import reverse
from pytest_django.asserts import assertContains, assertRedirects, assertTemplateUsed
import pytest

from .models import Student


@pytest.mark.django_db
def describe_home_page():
    def redirects_to_manage_students(client):
        response = client.get("/")
        assertRedirects(response, reverse("student_list"))

    def template_is_manage_students(client):
        response = client.get("/", follow=True)
        assertTemplateUsed(response, "student_list.html")


@pytest.mark.django_db
def describe_manage_students():
    student_list_url = reverse("student_list")

    def add_one_student(client):
        response = client.post(student_list_url, {"student-name": "dummy_student1"})
        assertContains(response, "dummy_student1")
        assertTemplateUsed(response, "student_list.html")

        assert Student.objects.count() == 1

        # TODO Redirect after Post

    def add_student_redirects_to_student_list(client):
        response = client.post(
            reverse("student_list"), {"student-name": "dummy_student1"}, follow=True
        )
        assertRedirects(response, reverse("student_list"))

    def add_two_students(client):
        response = client.post(student_list_url, {"student-name": "dummy_student1"})
        response = client.post(student_list_url, {"student-name": "dummy_student2"})
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
