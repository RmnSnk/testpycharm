import unittest
import main


class Arrondi(unittest.TestCase):
    def test_arrondi1(self):
        nbre = main.arrondi(0.1)
        self.assertEqual(nbre, 0)

    def test_arrondij2(self):
        nbre = main.arrondi(5.55)
        self.assertEqual(nbre, 5.5)

    def test_arrondi3(self):
        nbre = main.arrondi(9.89)
        self.assertEqual(nbre, 10)
