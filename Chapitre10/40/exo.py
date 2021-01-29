# coding:utf-8

"""Programme pour donner les 1000 premiers nombres premier, basé sur la méthode d'Eratosthène
   l'argement donné à la fonction liste fixe le nombres de nombres premiers que l'on cherche"""


def liste(n):
    """La fonction donne une liste de n éléments tous initialisé à 1
    Dans cette liste les indices des éléments représente nos entiers"""
    l = [1]
    return l * n


def trouvelespremier(liste_premiers):
    for i in range(2, len(liste_premiers)):
        """i ne présente pas l'élément en lui même mais son indice dans la liste"""
        if liste_premiers[i] == 1:
            """"Si l'élément de la liste vaut 1, on met à 0 tous ces multiple du reste de la liste"""
            for j in range(i + 1, len(liste_premiers)):
                if j % i == 0:
                    liste_premiers[j] = 0
    return liste_premiers


def affichage(liste):
    """La fonction convertie la liste binaire en liste des indices, qui représente les entiers"""
    l = []
    i = 0
    while i < len(liste):
        if liste[i] == 1:
            l.append(i)
            i +=1
        else:
            i+=1
    del l[0:2] # on enlève 0 et 1 qui ne sont pas des nombres premiers !!!!!!!
    return l


def main():
    n = int(input("Sur combien d'entier on travail ? : "))
    liste_brute = liste(n)
    liste_binaire = trouvelespremier(liste_brute)
    liste_entier = affichage(liste_binaire)
    print(liste_entier)



# TODO faire les tests unitairesi