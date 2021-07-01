from django.test import TestCase
from django.urls import resolve
from srs_app.views import home_page
from pytest_django.asserts import assertTemplateUsed


def describe_home_page():
    def template_is_available(client):
        assertTemplateUsed(client.get("/"), 'home.html')
