# coding:utf-8

import math

"""

Simple test de class

"""

class Point():
    """
    On fait rien, on définira les attributs à la volée
    """

def distance(p1, p2):

    distance_carré = (p2.x - p1.x)**2 + (p2.y - p1.y)**2

    return math.sqrt(distance_carré)

p1 = Point()
p2 = Point()

p1.x = 5
p1.y = 0

p2.x = 0
p2.y = 0

print(f"La distance entre les deux points est de {distance(p1, p2)}")