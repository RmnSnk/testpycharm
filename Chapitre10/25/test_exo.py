import unittest
import exo

class MyTestCase(unittest.TestCase):
    def test_mesure_sphere(self):
        sphere = exo.mesure_sphere(4)
        self.assertEqual(sphere, (8, 50.26548245743669, 201.06192982974676, 268.082573106329))



