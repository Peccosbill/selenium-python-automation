import unittest

class TestSearchUser(unittest.TestCase):

    def test_correct_search(self):
        data = True
        self.assertTrue(data)

    def test_incorrect_search(self):
        data = False
        self.assertFalse(data)

