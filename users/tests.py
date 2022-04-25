from django.test import TestCase

from users.views import add, subtract


class TestAdd(TestCase):
    def test_add(self):
        x = 4
        y = 5
        assert x + y == add(x, y)

    def test_subtract(self):
        x = 4
        y = 5
        assert x - y == subtract(x, y)
