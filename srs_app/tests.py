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
        assertTemplateUsed(response, STUDENT_LIST_TEMPLATE)


STUDENT_LIST_TEMPLATE = "student_list.html"
DUMMY_STUDENT = {"student-name": "dummy_student"}


@pytest.mark.django_db
def describe_manage_students():
    student_list_url = reverse("student_list")

    def describe_add_student():
        def saves_to_db(client):
            response = client.post(student_list_url, DUMMY_STUDENT, follow=True)
            assert Student.objects.count() == 1
            assert Student.objects.first().name == DUMMY_STUDENT["student-name"]

        def returns_valid_response_in_template(client):
            response = client.post(student_list_url, DUMMY_STUDENT, follow=True)
            assertContains(response, DUMMY_STUDENT["student-name"])
            assertTemplateUsed(response, STUDENT_LIST_TEMPLATE)


def describe_student_model():
    def create(db):
        student = Student.objects.create(name=DUMMY_STUDENT["student-name"])
        assert Student.objects.count() == 1
        assert student == Student.objects.first()
