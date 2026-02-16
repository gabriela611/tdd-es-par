# archivo de pruebas

import unittest
from mathUtils import esPar # no existe aun

class TestEsPar(unittest.TestCase):
    def test4esPar(self):
        self.assertTrue(esPar(4)) # 4 dbeeria ser par

    def test5esPar(self):
        self.assertFalse(esPar(5)) # 5 no dbeeria ser par

    def test0esPar(self):
        self.assertTrue(esPar(0)) # 0 si es

    def testNegativos(self):
        self.assertTrue(esPar(-2)) # si es
        self.assertFalse(esPar(-3)) # no es


if __name__ == "main":
    unittest.main()