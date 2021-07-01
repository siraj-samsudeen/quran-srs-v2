from django.test import TestCase

# Create your tests here.


class SmokeTest(TestCase):
    def test(self):
        assert 1 == 1


def test_func():
    assert 1 == 1
