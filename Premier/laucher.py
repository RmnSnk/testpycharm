# coding:utf-8

import exo
import argparse

""" Petit script pour comprendre et tester argparse
    si l'argument est précédé d'un tiret, c'est une option "-v". Sinon c'est un argument positionnel "x" """

parser = argparse.ArgumentParser()
parser.add_argument("n", type=int, help="La liste des nombres entiers de 0 à n")
parser.add_argument("-v", "--verbose", action="store_true", help="augmente le niveau de détail")

args = parser.parse_args()

if __name__ == '__main__':
    exo.main1(args.n)
    exo.main2(args.n)