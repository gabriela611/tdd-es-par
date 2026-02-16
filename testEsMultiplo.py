import unittest
from mathUtils import esMultiploDe # no existe aun

class TestEsMultiplo(unittest.TestCase):
    def test6EsMultiplo2(self):
        self.assertTrue(esMultiploDe(6,2)) # si es

    def test5Esmultiplo3(self):
        self.assertFalse(esMultiploDe(5,3)) # no es

    def testMultiplode0(self):
        self.assertFalse(esMultiploDe(2,0)) # no es
    
    def testNegativos(self):
        self.assertTrue(esMultiploDe(-2, 2)) # si es

    

    