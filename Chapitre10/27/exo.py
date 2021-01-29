# coding:utf-8

"""Script qui génère la liste des carrés et des cubes de 20 à 30"""

def mafonction():
    liste = range(20, 41)
    for i in liste:
        print(f"le carré de {i} est {i**2}, et le cube de {i} est {i**3}")

mafonction()