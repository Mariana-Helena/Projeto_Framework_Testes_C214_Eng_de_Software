from main import cafeicultor 

import unittest
from unittest import TestCase

class CafeicultorTest(TestCase):
    
    def setUp(self): 
        self.c1 = cafeicultor.Cafeicultor("João","3534-9965","15923678941","Itamogi","Sítio A","Banco do Brasil","8218-X","895-9")
        self.lista_cafeicultores = []

    def test_cafeicultor(self):
        self.assertEqual("João",self.c1.nome)
        self.assertTrue(self.c1.nome)
    
    def test_arrayVazio(self):
        self.assertEqual(0,len(self.lista_cafeicultores))

    def test_arrayAppend(self):
        self.lista_cafeicultores.append(self.c1)
        self.assertEqual(1,len(self.lista_cafeicultores))
        self.assertIn(self.c1,self.lista_cafeicultores)

    def test_arrayPop(self):
        self.lista_cafeicultores.append(self.c1)
        expected = self.lista_cafeicultores.pop()
        self.assertEqual(self.c1,expected)
        self.assertEqual(0,len(self.lista_cafeicultores))
        self.assertNotIn(self.c1,self.lista_cafeicultores)

    def test_arrayException(self):
        with self.assertRaises(IndexError):
            self.lista_cafeicultores.pop()

    

if __name__ == "__main__":
    unittest.main()







