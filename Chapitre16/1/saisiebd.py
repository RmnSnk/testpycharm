# coding:utf-8

import sqlite3
import csv

"""

Module contenant des class et des fonctins pour alimenter la base de donnée

"""

class Musicien():

    def __init__(self, nom, a_naiss, a_mort):
        self.nom = nom
        self.a_naiss = a_naiss
        self.a_mort = a_mort


def creation_table_compositeur(nom_table='compositeur'):

    """
    Efface la table nom_table et en recrée une vierge
    :param nom_table: par défaut celui de l'xo
    :return: rien, procédure pour remplir la table
    """

    bdd = '/home/romain/PycharmProjects/testpycharm/Chapitre16/1/bdd.sq3'

    requete_suppression = str(f"DROP TABLE {nom_table}")
    requete_creation = str(f"CREATE TABLE {nom_table} (comp TEXT, a_naiss INTEGER, a_mort INTEGER)")
    conn = sqlite3.connect(bdd)
    cur = conn.cursor()


    try:
        cur.execute(requete_suppression)
    except sqlite3.OperationalError:
        pass

    cur.execute(requete_creation)
    conn.commit()

    cur.close()
    conn.close()

def creation_table_oeuvres(nom_table='oeuvres'):

    """

    :param nom_table:
    :return: rien procédure pour remplir la table
    """

    bdd = '/home/romain/PycharmProjects/testpycharm/Chapitre16/1/bdd.sq3'
    f_csv = '/home/romain/PycharmProjects/testpycharm/Chapitre16/1/oeuvres.csv'

    requete_suppression = str(f"DROP TABLE {nom_table}")
    requete_creation = str(f"CREATE TABLE {nom_table} (comp TEXT, titre TEXT, duree INTEGER, interpr TEXT)")


    conn = sqlite3.connect(bdd)
    cur = conn.cursor()

    try:
        cur.execute(requete_suppression)
    except sqlite3.OperationalError:
        pass

    cur.execute(requete_creation)

    conn.commit()

    cur.close()
    conn.close()



def ajout_compositeur(musicien):

    """
    Permet de saisir dans la table Compositeurs de la bdd les informations sur les musiciens
    musicien est une instance de la classe Musicien
    :return: rien
    """
    bdd = '/home/romain/PycharmProjects/testpycharm/Chapitre16/1/bdd.sq3'
    conn = sqlite3.connect(bdd)
    cur = conn.cursor()

    requete = str(f"INSERT INTO compositeur (comp, a_naiss, a_mort) VALUES{musicien.nom, musicien.a_naiss, musicien.a_mort}") # Remarquons l'absence de () pour value ...
    #print(requete)

    cur.execute(requete)
    conn.commit()

    cur.close()
    conn.close()

def ajout_oeuvres():

    f_csv = '/home/romain/PycharmProjects/testpycharm/Chapitre16/1/oeuvres.csv'
    bdd = '/home/romain/PycharmProjects/testpycharm/Chapitre16/1/bdd.sq3'

    conn = sqlite3.connect(bdd)
    cur = conn.cursor()

    with open(f_csv, encoding='utf-8', newline='') as f:
        reader = csv.reader(f)
        next(reader)  # Pour avant l'itérateur de reader de 1 avant la boucle et virer la première colone
        for ligne in reader:

            oeuvres = 'oeuvres'
            cur.execute(f"INSERT INTO {oeuvres} VALUES (?,?,?,?)", ligne)

    conn.commit()
    cur.close()
    conn.close()



def lecture_table(table):

    """
    :param table: nom de la table de la bbd à lire
    :return: la table
    """
    bdd = '/home/romain/PycharmProjects/testpycharm/Chapitre16/1/bdd.sq3'
    conn = sqlite3.connect(bdd)
    cur = conn.cursor()

    requete = str(f"SELECT * FROM {table}")
    #print(requete)
    cur.execute(requete)
    for l in cur:
        print(l)

    cur.close()
    conn.close()




# Test rapide
if __name__ =='__main__':

    # Pour tester la table compositeurs
    #mozart = Musicien('Mozart', 1756, 1791)
    #creation_table_compositeur()
    #ajout_compositeur(mozart)


    # Pour tester la table oeuvres
    creation_table_oeuvres()
    oeuvre = ('Vivaldi', 'Les quatre saison', 20, 'T. Pinnock')
    ajout_oeuvre(oeuvre)
    lecture_table('oeuvres')

# TODO : Faire une boucle qui va, à partir une liste d'oeuvre dans un fichier cvs, remplir automatiquement la table oeuvre. Commencer par écrire le fichier cvs


