# coding:utf-8

import argparse

""" Petit script pour comprendre et tester argparse
    si l'argument est précédé d'un tiret, c'est une option "-v". Sinon c'est un argument positionnel "x" """

parser = argparse.ArgumentParser()
parser.add_argument("x", type=int, help="Le nombre a élever au carré, doit être un entier")
parser.add_argument("-v", "--verbose", action="store_true", help="augmente le niveau de détail")

args = parser.parse_args()
print("Vous avez précisé X=", args.x)