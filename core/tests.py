from django.test import TestCase


def add_num(num):
    return num + 1


class Simple(TestCase):
    def setUp(self):
        print('started')

    def test_add_num(self):
        value = add_num(3)
        self.assertTrue(value == 4)
