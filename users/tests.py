from django.test import TestCase

from users.views import add


class TestAdd(TestCase):
    def test_add(self):
        x = 4
        y = 5
        assert x + y == add(x, y)
