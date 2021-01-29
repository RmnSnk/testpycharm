# coding:utf-8

"""Programme qui affihce la table du multiplication des nombres entiers"""


def table(x):
    l = list()
    for i in range(1, 11):
        l.append(str(i * x):4d)  # TODO : convertir l en chaine de caractère avec join pour avoir affichage plus sympa
    l = " ".join(l)
    return l


liste = "2 3 5 7 11 13 17 19"

l = liste.split()

for i in l:
    i = int(i)
    print(table(i))



