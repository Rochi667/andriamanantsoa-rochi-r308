import os
from getpass import getpass

from partie_c import FICHIER_MOTS, charger_mots, choisir_mot, masque

ERREURS_MAX = 7
DOSSIER = os.path.dirname(os.path.abspath(__file__))
FICHIER_SCORES = os.path.join(DOSSIER, "scores.txt")
PIECES = ["|", "O", "|", "/", "\\", "/", "\\"]  # ajoutées une par erreur
ACCENTS = {"É": "E", "È": "E", "Ê": "E", "À": "A", "Â": "A",
           "Î": "I", "Ô": "O", "Û": "U", "Ç": "C"}


def sans_accent(lettre):
    """É -> E. Une lettre sans accent reste inchangée."""
    return ACCENTS.get(lettre, lettre)


def dessin(erreurs):
    """Le pendu en ASCII art, selon le nombre d'erreurs."""
    p = [" "] * 7
    for i in range(erreurs):
        p[i] = PIECES[i]
    return (f"  +---+\n  {p[0]}   |\n  {p[1]}   |\n"
            f" {p[3]}{p[2]}{p[4]}  |\n {p[5]} {p[6]}  |\n      |\n=========")


def lire_lettre(proposees):
    """Redemande tant que ce n'est pas UNE lettre jamais proposée."""
    while True:
        lettre = sans_accent(input("Lettre : ").strip().upper())
        if len(lettre) != 1 or not lettre.isalpha():
            print("Entre UNE seule lettre.")
        elif lettre in proposees:
            print("Déjà proposée, pas de pénalité.")
        else:
            return lettre


def reveler(mot, lettre, cache):
    """Montre la lettre dans le masque. Renvoie True si elle est dans le mot."""
    trouve = False
    for i in range(len(mot)):
        if sans_accent(mot[i]) == lettre:
            cache[i] = mot[i]  # on garde la vraie lettre, avec son accent
            trouve = True
    return trouve


def afficher(cache, erreurs, proposees):
    """Dessin, mot masqué, erreurs et lettres déjà proposées."""
    print()
    print(dessin(erreurs))
    print("Mot     :", " ".join(cache))
    print(f"Erreurs : {erreurs}/{ERREURS_MAX}")
    print("Lettres :", " ".join(proposees))


def jouer_partie(mot):
    """Une partie. Renvoie True si le joueur gagne."""
    cache = masque(mot)
    erreurs = 0
    proposees = []

    while erreurs < ERREURS_MAX and "_" in cache:
        afficher(cache, erreurs, proposees)
        lettre = lire_lettre(proposees)
        proposees.append(lettre)
        if not reveler(mot, lettre, cache):
            erreurs += 1

    afficher(cache, erreurs, proposees)
    if "_" in cache:
        print("Perdu, le mot était", mot)
        return False
    print("Gagné !")
    return True


def charger_scores(chemin):
    """Lit nom:victoires. Ignore les lignes invalides. Absent : {}."""
    scores = {}
    try:
        with open(chemin, encoding="utf-8") as f:
            for ligne in f:
                morceaux = ligne.strip().split(":")
                if len(morceaux) != 2:
                    continue
                try:
                    scores[morceaux[0]] = float(morceaux[1])
                except ValueError:
                    pass
    except OSError:
        pass  # premier lancement : on part de zéro
    return scores


def sauvegarder_scores(chemin, scores):
    """Écrit une ligne nom:victoires par joueur."""
    try:
        with open(chemin, "w", encoding="utf-8") as f:
            for nom, victoires in scores.items():
                f.write(f"{nom}:{victoires}\n")
    except OSError:
        print("Sauvegarde des scores impossible.")


def mot_du_tour(mots):
    """Mode 2 joueurs : un ami tape le mot (caché), sinon mot au hasard."""
    if input("Mot choisi par un ami ? (o/n) : ").strip().lower() == "o":
        mot = getpass("Mot secret (caché) : ").strip().upper()
        if mot.isalpha():
            return mot
        print("Mot invalide (lettres seulement) : mot au hasard.")
    return choisir_mot(mots)


def main():
    mots = charger_mots(FICHIER_MOTS)
    scores = charger_scores(FICHIER_SCORES)
    nom = input("Ton nom : ").strip().replace(":", "") or "Anonyme"

    rejouer = "o"
    while rejouer == "o":
        if jouer_partie(mot_du_tour(mots)):
            scores[nom] = scores.get(nom, 0.0) + 1
            sauvegarder_scores(FICHIER_SCORES, scores)
        print("\n--- Hall of fame ---")
        for joueur, victoires in scores.items():
            print(f"{joueur} : {int(victoires)}")
        rejouer = input("Rejouer ? (o/n) : ").strip().lower()


if __name__ == "__main__":
    main()