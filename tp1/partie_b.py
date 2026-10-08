"""Partie B : Devine le nombre."""

import random

ESSAIS_MAX = 10


def demander_entier(message):
    """Redemande tant que la saisie n'est pas un entier."""
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Entre un nombre entier.")


def jouer(mini, maxi):
    """Une partie. Renvoie True si le joueur gagne."""
    secret = random.randint(mini, maxi)
    print(f"Devine le nombre entre {mini} et {maxi} ({ESSAIS_MAX} essais).")

    for essai in range(1, ESSAIS_MAX + 1):
        proposition = demander_entier(f"Essai {essai}/{ESSAIS_MAX} : ")
        if proposition < secret:
            print("Trop petit")
        elif proposition > secret:
            print("Trop grand")
        else:
            print("Gagné en", essai, "essai(s) !")
            return True

    print("Perdu, le nombre était", secret)
    return False


def main():
    rejouer = "o"
    while rejouer == "o":
        mini = demander_entier("Borne minimale : ")
        maxi = demander_entier("Borne maximale : ")
        if mini >= maxi:
            print("La borne minimale doit être plus petite que la maximale.")
            continue
        jouer(mini, maxi)
        rejouer = input("Rejouer ? (o/n) : ").strip().lower()


if __name__ == "__main__":
    main()