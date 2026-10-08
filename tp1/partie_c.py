import os
import random

MOTS_PAR_DEFAUT = ["python", "reseau", "ordinateur", "clavier", "serveur"]
DOSSIER = os.path.dirname(os.path.abspath(__file__))
FICHIER_MOTS = os.path.join(DOSSIER, "mots.txt")


def charger_mots(chemin):
    """Lit un mot par ligne. Fichier absent ou vide : liste par défaut."""
    mots = []
    try:
        with open(chemin, encoding="utf-8") as f:
            for ligne in f:
                mot = ligne.strip()
                if mot:  # ignore les lignes vides
                    mots.append(mot)
    except OSError:
        print(chemin, "introuvable : liste par défaut utilisée.")
    if not mots:
        return MOTS_PAR_DEFAUT
    return mots


def choisir_mot(liste):
    """Choisit un mot au hasard, en MAJUSCULES."""
    return random.choice(liste).upper()


def masque(mot):
    """Une liste de '_' de la même longueur que le mot."""
    return ["_"] * len(mot)


if __name__ == "__main__":
    mot = choisir_mot(charger_mots(FICHIER_MOTS))
    print("Mot choisi :", mot)
    print("Masque :", masque(mot))
    print(masque("PYTHON"))