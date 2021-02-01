# coding:utf-8

import random

def trie(nombre, fraction):
    
    """"
    La fonction trie attend deux paramètres : 
    nombre : le nombre d'éléments à tirer
    fraction : ne nombre d'intervals dans lesquels trier les valeurs
    Elle retourne la liste du nombre d'occurence par fraction
    """

    compteur_fraction = [0] * fraction
    for i in range(nombre):
        valeur = random.random()
        l = numeroFraction(valeur, fraction, compteur_fraction)
    return l



def numeroFraction(valeur, fraction, compteur_fraction):
    
    """
    
    :param valeur: la valeur choisie au hasard
    :param fraction: la nombre d'intervals
    :return: la fraction à laquelle appartien la valeur
    On va utiliser la technique int(valeur * nombre de fraction) = index de la fraction
    et int(un float) renvoie la partie entière du float

    """
    
    indice = int((valeur * fraction))
    compteur_fraction[indice] += 1
    return compteur_fraction


def affichage(l):

    """

    :param l: la liste à afficher

    La méthode .index(elt) est utilisée pour retrouver l'index de l'élément d'une liste.

    """

    for elt in l:
        print(f"La catégorie {l.index(elt) + 1} contient {elt} éléments")


def main(nombre, fraction):
    #nombre = int(input("Le nombre de tirage ? : "))
    #fraction = int(input("Le nombre de fraction ? : "))
    l = trie(nombre, fraction)
    affichage(l)