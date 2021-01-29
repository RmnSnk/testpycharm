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


def main1(n):

    """Assemble le programme et renvoi la liste de tous les nombres premier de 0 à n"""

    liste_brute = liste(n)
    liste_binaire = trouvelespremier(liste_brute)
    liste_entier = affichage(liste_binaire)
    print(liste_entier)


def main2(n):

    """Renvoi false si le nombre n'est pas entier, true sinon
    Pour le savoir on cherche tous les nombre premier entre 0 et n/2 en effet après la division donnera
    forcement un dividende inférieur à 2 et donc"""

    liste_diviseur = affichage(trouvelespremier(liste(1+(n//2))))

    flag = 0
    diviseurs = []
    for i in liste_diviseur:
        a = n % i
        if a == 0:
            flag += 1
            diviseurs.append(str(i))
    if flag == 0:
        return print(f"{n} nombre est premier")
    else:
        diviseurs = ", ".join(diviseurs)
        return print(f"{n} n'est pas premier, ses diviseurs premiers sont : {diviseurs}")

