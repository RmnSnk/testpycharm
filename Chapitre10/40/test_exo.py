import unittest
import exo

class MyTestCase(unittest.TestCase):
    def test_liste(self):
        l = exo.liste(3)
        a = [1, 1, 1]
        self.assertEqual(l, a)

    def test_trouvelespremiers(self):
        l = exo.trouvelespremier([1]*20)
        a = [1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1]
        self.assertEqual(l, a)

    def test_affichage(self):
        l = exo.affichage([1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1])
        a = [2, 3, 5, 7, 11, 13, 17, 19]
        self.assertEqual(l, a)



