# coding:utf-8

import exo
import argparse

""" Petit script pour comprendre et tester argparse
    si l'argument est précédé d'un tiret, c'est une option "-v". Sinon c'est un argument positionnel "x" 
    
    Un seul argument positionnel :
    n  : basiquement c'est l'entier à tester : on cherche si c'est un nombre premier ou pas
    
    Deux arguments optionnels: 
    -v : donne en plus la liste de tous les nombres entier entre 0 et n
    -l : ne dit pas si le nombre n est premier mais renvoie la liste de tous les nombres premiers entre 0 et n
    """

parser = argparse.ArgumentParser()
parser.add_argument("n", type=int, help="Dit si un nombre est premier et renvoie la liste de ses diviseurs premiers")
parser.add_argument("-v", "--verbose", action="store_true", help="Renvoie également la liste de tous les chiffres premiers de 0 à n")
parser.add_argument("-l", "--liste", action="store_true", help="Si l'option est précisé, ne renvoie que la liste des chiffres premiers de 0 à n")

args = parser.parse_args()
n = args.n


if __name__ == '__main__':

    if args.verbose: # si arg.verbose est vrai ie, si -v a été précisé "store_true"
        exo.main2(n)
        exo.main1(n)
    else:
        if args.liste:
            exo.main1(n)
        else:
            exo.main2(n)
