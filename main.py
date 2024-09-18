"""
Nom : Lucas Beaudry Tinkler
Groupe : 401
Détail : jeu de devinettes (trouver un nombre entre deux extremes que vous choisissez)
"""

import random


def une_partie(min, max):
    nbr_aleatoir = random.randint(min, max)
    nbr_essai = 0

    print(f"J'ai choisis un nombre entre {min} et {max}\nÀ vous de le deviner...")
    essai = 0

    while essai != nbr_aleatoir:
        essai = int(input("\nEntrez votre essai :"))
        nbr_essai += 1
        if essai > nbr_aleatoir:
            print(f"Mauvais choix, le nombre est plus petit que {essai}")
        elif essai < nbr_aleatoir:
            print(f"Mauvais choix, le nombre est plus grand que {essai}")
        else:
            print(f"Bravo! Bonne réponse\nVous avez réussi en :{nbr_essai} essai(s)")


while True:
    min = int(input("Choisissez un minimum : "))
    max = int(input("Choisissez un maximum : "))
    une_partie(min, max)
    nouvelle_partie = input("Voulez-vous faire une autre partie (o/n)?: ")
    if nouvelle_partie == "o":
        print("bonne chance!")
    else:
        print("Merci et au revoir")
        break
