import os

DOSSIER = os.path.dirname(os.path.abspath(__file__))
FICHIER = os.path.join(DOSSIER, "etudiants.txt")


def ajouter_etudiant(d, nom, note):
    """Ajoute l'étudiant, ou met à jour sa note s'il existe déjà."""
    d[nom] = float(note)


def moyenne_classe(d):
    """Moyenne des notes (0.0 si le dictionnaire est vide)."""
    if not d:
        return 0.0
    return sum(d.values()) / len(d)


def meilleur_etudiant(d):
    """Renvoie (nom, note) du meilleur, ou None si le dictionnaire est vide."""
    meilleur = None
    for nom, note in d.items():
        if meilleur is None or note > meilleur[1]:
            meilleur = (nom, note)
    return meilleur


def sauvegarder(d, chemin):
    """Écrit une ligne nom:note par étudiant."""
    try:
        with open(chemin, "w", encoding="utf-8") as f:
            for nom, note in d.items():
                f.write(f"{nom}:{note}\n")
    except OSError:
        print("Impossible d'écrire dans", chemin)


def charger(chemin):
    """Lit le fichier. Ignore les lignes mal formées. Fichier absent : {}."""
    d = {}
    try:
        with open(chemin, encoding="utf-8") as f:
            for ligne in f:
                morceaux = ligne.strip().split(":")
                if len(morceaux) != 2:
                    continue  # ligne mal formée
                try:
                    d[morceaux[0]] = float(morceaux[1])
                except ValueError:
                    pass  # note qui n'est pas un nombre
    except OSError:
        print(chemin, "absent : départ avec un dictionnaire vide.")
    return d


if __name__ == "__main__":
    etudiants = {}
    ajouter_etudiant(etudiants, "Alice", 12)
    ajouter_etudiant(etudiants, "Bob", 15)
    ajouter_etudiant(etudiants, "Claire", 9.5)
    print(etudiants)
    print("Moyenne :", round(moyenne_classe(etudiants), 2))
    print(meilleur_etudiant(etudiants))

    sauvegarder(etudiants, FICHIER)
    print(charger(FICHIER))

    print(moyenne_classe({}), meilleur_etudiant({}))  # cas vide
    print(charger("inexistant.txt"))   