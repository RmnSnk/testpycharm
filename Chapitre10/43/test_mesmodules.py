import unittest
import mesmodules


class MyTestCase_trie(unittest.TestCase):

    """On va tester si la fonction renvoie ce qui est attendue"""

    def test_trie(self):
        """ On test si le nombre de classe est bien celui attendu"""
        l = mesmodules.trie(100, 7)
        l_len = len(l)
        self.assertEqual(l_len, 7)

    def test_trie_nombrefraction(self):
        """ On test si le total des occurences par classe est bien égal au nombre choisi"""
        l = mesmodules.trie(100, 7)
        compteur = 0
        for element in l:
            compteur += element
        self.assertEqual(compteur, 100)


class MyTestCase_numeroFraction(unittest.TestCase):

    def test_numeroFraction(self):
        """On test que c'est le bon élement de la liste qui est incrémenter"""
        l = mesmodules.numeroFraction(0.774, 3, [3, 8, 0])
        l_test = [3, 8, 1]
        self.assertEqual(l, l_test)





if __name__ == '__main__':
    unittest.main()
