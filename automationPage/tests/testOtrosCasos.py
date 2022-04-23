import unittest


class Pruebas_de_standards(unittest.TestCase):

    def test_otra_suma_II(self):
        a = 2 + 2
        b = 3 + 1
        self.assertEqual(a, b)

    def test_otra_suma_III(self):
        a = 5 + 1
        b = 5 + 2
        self.assertNotEqual(a, b)

    def test_algo_es_verdadero(self):
        a = 5 + 1
        b = 4 + 2
        self.assertTrue(a == b, "a y b deberían ser iguales")
