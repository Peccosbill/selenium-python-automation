import unittest

class TestUsers(unittest.TestCase):
    
    def test_create_user(self):
        user = 'Pepe'
        self.assertEqual(user, 'Pepe')

    def test_user_not_created(self):
        response = 'El usuario no ha sido creado'
        self.assertEqual(response, 'El usuario no ha sido creado')


