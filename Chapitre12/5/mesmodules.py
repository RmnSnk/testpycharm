# coding:utf-8

import math

"""

Bibliothèque de class et fonction pour l'exercice

"""

class Cercle():

    """"

    Cette class permet d'intancier des cercles par leur rayon

    """

    def __init__(self, rayon):

        self.rayon = rayon


    def surface(self):

        """
        :return: La surface de l'objet

        """

        surface = math.pi * self.rayon ** 2
        return surface


class Cylindre(Cercle):

    """

    Cette classe hérite de Cercle et défini un cylindre

    """

    def __init__(self, rayon, hauteur):

        Cercle.__init__(self, rayon)
        self.hauteur = hauteur
        self.nom = "cylindre"


    def volume(self):

        volume = self.surface() * self.hauteur
        return volume

    def __str__(self):

        return (f"Le rayon du {self.nom} est de {self.rayon:.2f} et son volume est de {self.volume():.2f} unité au cube")


class Cone(Cylindre):

    """

    Bon ce coup ci c'est un cone ...
    On triche en renvoyant une hauteur divisée par 3 afin de ne pas avoir à réécrire la méthode volume

     """

    def __init__(self, rayon, hauteur):

        Cylindre.__init__(self, rayon, hauteur/3)
        self.nom = "cone"