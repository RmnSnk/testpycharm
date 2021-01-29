# coding:utf-8

import random


def création_fichier():
    """Procédure qui écrit dix chiffres réels de taille variée dans un fichier texte"""

    f = open("liste_reel.txt", 'w')
    for i in range(10):
        a = random.randint(1, 10000)
        b = random.randint(1, 100)
        c = a / b
        f.write(str(c) + '\n')
    f.close()


def arrondi(nbre):
    partie_entiere = int(nbre)
    partie_decimale = nbre - partie_entiere
    if partie_decimale < 0.5:
        partie_decimale = 0
    elif partie_decimale < 0.75:
        partie_decimale = 0.5
    else:
        partie_decimale = 0
        partie_entiere += 1
    return (partie_entiere + partie_decimale)



def copie():
    """On récupère la ligne de fichier et on la formate en réél en enlevant le \n final"""
    fr = open("liste_reel.txt", 'r')
    fw = open("copie.txt", 'w')

    for element in fr:
        ligne = float(element)
        ligne = arrondi(ligne)
        fw.write(str(ligne) + '\n')
        print(ligne)
        #fw.write(ligne)

    fr.close()
    fw.close()


création_fichier()
copie()
