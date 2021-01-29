import unittest
import exo

class MyTestCase(unittest.TestCase):
    def test_table(self):
        a = exo.table(4)
        l = [4, 8, 12, 16, 20, 24, 28, 32, 36, 40]
        self.assertEqual(a, l)


