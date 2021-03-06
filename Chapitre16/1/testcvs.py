# coding utf-8

import csv
import sqlite3

f_csv = '/home/romain/PycharmProjects/testpycharm/Chapitre16/1/oeuvres.csv'
bdd = '/home/romain/PycharmProjects/testpycharm/Chapitre16/1/bdd.sq3'



conn = sqlite3.connect(bdd)
cur = conn.cursor()

with open(f_csv, encoding='utf-8', newline='') as f:
    reader = csv.reader(f)
    next(reader) # Pour avant l'itérateur de reader de 1 avant la boucle et virer la première colone
    for ligne in reader:
        print(ligne)
        #requete = str(f"INSERT INTO oeuvres VALUES {ligne[0], ligne[1], ligne[2], ligne[3]}")
        #cur.execute(requete)

        #Pour tester les f-strings
        oeuvres = 'oeuvres'

        cur.execute(f"INSERT INTO {oeuvres} VALUES (?,?,?,?)", ligne)

conn.commit()
cur.close()
conn.close()