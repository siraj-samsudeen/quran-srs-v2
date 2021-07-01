from django.test import TestCase
from django.urls import resolve
from srs_app.views import home_page


def describe_home_page():
    def url_is_valid():
        assert resolve("/").func == home_page
