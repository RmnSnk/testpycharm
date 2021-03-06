# -*- coding: utf-8 -*-
"""
Programme principal

"""
import saisiebd as sbd
import sqlite3


LISTE_MUSICIENS = [

    ('Mozart', 1756, 1791),
    ('Beethoven', 1770, 1827),
    ('Haendel', 1685, 1759),
    ('Schubert', 1797, 1828),
    ('Vivaldei', 1678, 1741),
    ('Monteverdi', 1567, 1643),
    ('Chopin', 1810, 1849),
    ('Bach', 1685, 1750),
    ('Shostokovich', 1906, 1975)
    ]


# On commence par demander si on dit créer une nouvelle table "compositeur et une nouvelle table oeuvres"
reset = input("Souhaitez vous effacer la base (O/N) ? : ")
if reset == 'O':
    sbd.creation_table_compositeur() # On efface et on recrée une table "compositeur" vierge

    # On importe la liste des musiciens dans la table à partir de la liste LISTE_MUSICIENS
    for element in LISTE_MUSICIENS:
        musicien = sbd.Musicien(element[0], element[1], element[2])
        sbd.ajout_compositeur(musicien)

    sbd.creation_table_oeuvres() # On efface et on recrée une table "oeuvres" vierge
    sbd.ajout_oeuvres() # et on la remplit avec le fichier CVS


def saisie():

    """

    :return: Ce retour de la requete SQL
    """


    bdd = '/home/romain/PycharmProjects/testpycharm/Chapitre16/1/bdd.sq3'
    conn = sqlite3.connect(bdd)
    cur = conn.cursor()
    requete = 'toto'

    while requete != '':
        requete = input("Requête SQL : ")
        try:
            cur.execute(requete)
            for l in cur:
                print(l)
        except:
            pass

    conn.commit()
    cur.close()
    conn.close()


#sbd.lecture_table("compositeur")
#sbd.lecture_table("oeuvres")

saisie()



