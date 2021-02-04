# coding:utf-8

"""Programme qui permet de simuler une base de donnée en lecture / écriture grâce à un dictionnaire"""

import pickle as pick

def saisir(dictionnaire):

    """

    On envoie en paramètre les données à ajouter au dictionnaire et renvoie le dictionnaire complété
    :param dictionnaire:
    :return: le dictionnaire avec la nouvelle entrée
    """

    prénom = input("Prénom ? : ")
    nom = input("Nom ? : ")
    age = int(input("Age ? : "))
    taille = float(input("Taille  ? :"))

    clef = prénom + " " + nom
    valeur = (age, taille)
    dictionnaire[clef] = valeur

    return dictionnaire

def afficher(dictionnaire):

    """

    :param nom:
    :param dictionnaire:
    :return: la liste des élèves (leur nom)
    """
    print("Les élèves présents dans la base de donnée sont : ")
    for k in dictionnaire:
        print(f"{k:^30}")


def consulter(dictionnaire):

    """

    :param dictionnaire: Le nom du dictionnaire
    :return: Renvoi une ligne de texte formaté qui contier le nom compler, l'âge et la taille de l'élève

    """
    afficher(dictionnaire)
    print("\n")

    choix = input("Merci de saisir le nom de l'élève : ")
    if choix in dictionnaire:
        print(f" L'élève {choix} à {dictionnaire[choix][0]} ans et mesure {dictionnaire[choix][1]:.2f} mètres")
    else:
        print("\n")
        print(f"L'élève {choix} est inconnu, merci de choisir un élève dans la liste si dessous")
        afficher(dictionnaire)



def menu(dictionnaire):

    """
    Fonction pour demander à l'utilisateur ce qu'il souhaite faire

    :return:
    """


    print("\n"
          "1. Affiche la liste des élèves \n"
          "2. Consulter l'âge et la taille d'un élève \n"
          "3. Saisir un nouvel élève \n"
          "4. Quitter \n"
              )
    choix = int(input("Merci de saisir 1, 2, 3 ou 4 : "))

    if choix == 1:
        print("\n")
        afficher(dictionnaire)
        menu(dictionnaire)
    elif choix == 2:
        print("\n")
        consulter(dictionnaire)
        menu(dictionnaire)
    elif choix == 3:
       print("\n")
       saisir(dictionnaire)
       menu(dictionnaire)
    else:
        enregistrement(dictionnaire)
        print("Fichier enregistré")
        exit()

def enregistrement(dictionnaire):

    """

    :param dictionnaire: le dictionnaire à sauvegarder
    :return:
    """
    with open('dictionnaire', 'wb') as fichier:
        mon_pickler = pick.Pickler(fichier)
        mon_pickler.dump(dictionnaire)


def lecture():

    """

    :return: le dictionnaire
    """

    with open('dictionnaire', 'rb') as fichier:
        mon_depickler = pick.Unpickler(fichier)
        dictionnaire = mon_depickler.load()

        return dictionnaire





def main(dictionnaire):

    """
    Aseemble de notre programme
    :return: rien
    """

    menu(dictionnaire)



dictionnaire = lecture()
main(dictionnaire)