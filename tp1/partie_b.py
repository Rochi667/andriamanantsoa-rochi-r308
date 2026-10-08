import random

NB_ESSAIS_MAX = 10


def demander_entier(message):
    while True:
        texte = input(message)
        try:
            return int(texte)
        except ValueError:
            print("Entre un nombre entier.")


def jouer(borne_min, borne_max):
    secret = random.randint(borne_min, borne_max)
    print(f"Devine le nombre entre {borne_min} et {borne_max} ({NB_ESSAIS_MAX} essais).")

    for essai in range(1, NB_ESSAIS_MAX + 1):
        proposition = demander_entier(f"Essai {essai}/{NB_ESSAIS_MAX} : ")

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
    rejouer = True
    while rejouer:
        borne_min = demander_entier("Borne minimale : ")
        borne_max = demander_entier("Borne maximale : ")
        if borne_min >= borne_max:
            print("La borne minimale doit être plus petite que la maximale.")
            continue
        jouer(borne_min, borne_max)
        rejouer = input("Rejouer ? (o/n) : ").strip().lower() == "o"


main()