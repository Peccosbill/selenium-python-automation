import unittest


class Pruebas_de_standards(unittest.TestCase):

    def test_suma(self):
        a = 2 + 2
        b = 3 + 1
        self.assertEqual(a, b)

    def test_otra_suma(self):
        a = 5 + 1
        b = 5 + 2
        self.assertNotEqual(a, b)

    def test_algo_es_verdadero(self):
        a = 5 + 1
        b = 4 + 2
        self.assertTrue(a == b, "a y b deberían ser iguales")

    def test_algo_es_falso(self):
        self.assertFalse(2+1 == 3+5)

    def test_algo_es_mayor(self):
        a = 5
        b = 3
        self.assertGreater(a, b)

    def test_comparar_listas(self):
        a = [1,2,3,4]
        b = [1,2,3,4]
        self.assertListEqual(a,b)

    def test_comparar_tuplas(self):
        a = (1,2,3,4)
        b = (1,2,3,4)
        self.assertTupleEqual(a,b)

    def test_comparar_diccionario(self):
        a = {"id":1, "nombre": "jony", "appellido": "montini"}
        b = {"id":1, "nombre": "jony", "appellido": "montini"}
        self.assertDictEqual(a,b)

if __name__ == '__main__':
    unittest.main()
