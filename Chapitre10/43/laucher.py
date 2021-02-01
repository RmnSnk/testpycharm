# coding:utf-8

import mesmodules
import argparse

""" 

Le script va lancer le programmme principal. Il comprend Deux arguments optionnels : 
-n : le nombre de valeurs à trier : minimum 1, 1000 par défaut
-p : le nombre de fractions pour effectuer le trie : minimum 2, 5 par défaut

"""

parser = argparse.ArgumentParser()
parser.add_argument("-n", "--nombre", type=int, help="Le nombre de valeurs à trier")
parser.add_argument("-p", "--partie", type=int, help="Le nombre de fraction souhaitée")


args = parser.parse_args()
n = args.nombre # Si on récupère des arguments optionnels, on doit les écrire en entier
p = args.partie

if n == None:
    n = 1000
if p == None:
    p = 5


if __name__ == '__main__':
    mesmodules.main(n, p)

# Todo : coder laucher pour prendre des arguments
