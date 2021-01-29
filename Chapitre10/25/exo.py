# coding:utf-8

from math import pi

fl = open("sphere.txt", 'r')
rayon = fl.readline()


def mesure_sphere(r):
    diametre = r*2
    section = pi*r**2
    surface = 4*pi*r**2
    volume =  (4/3)*pi*r**3
    return diametre, section, surface, volume

#liste = mesure_sphere(4)
#print(f"Diam {liste[0]:.2f} cm Section {liste[1]:.2f} cm Surface {liste[2]:.2f} Volume {liste[3]:.2f}")
#print(liste)


fr = open("sphere.txt", 'r')
fw = open("calcul.txt", 'w')

for element in fr:
    rayon = float(element)
    liste = mesure_sphere(rayon)
    line = (f"Diam {liste[0]:.2f} cm Section {liste[1]:.2f} cm Surface {liste[2]:.2f} Volume {liste[3]:.2f}" + '\n')
    fw.write(line)

fr.close()
fw.close()