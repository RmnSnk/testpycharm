# coding:utf-8

import random
import math


"""Programme qui reprend la technique de Monté Carlo pour estimer pi"""

def pointM():
    x = random.random()
    y = random.random()
    c = list()
    c.append(x)
    c.append(y)
    return c


def statistiques(nbre_test):
    danslecercle = 0
    pasdanslecercle = 0


    for i in range(nbre_test + 1):
        m = pointM()
        d = math.sqrt(m[0] ** 2 + m[1] ** 2)
        if d == 1:
            pass
        elif d < 1:
            danslecercle += 1
        else:
            pass

    try:
        estimationpi = danslecercle / nbre_test
    except ZeroDivisionError:
        print("Essayer avec un nombre plus grand ! Aucun point en dehors du cercle !")

    return estimationpi


a = int(input("Combien de test voulez vous faire ? : "))
estimation = statistiques(a)

pi = 4 * estimation

print(f"L'estimation de la valeur de pi : {pi:.5f}")








