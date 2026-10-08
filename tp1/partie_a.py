import os

# Le fichier est créé à côté du script, quel que soit le dossier de lancement
FICHIER = os.path.join(os.path.dirname(os.path.abspath(__file__)), "etudiants.txt")


def convertir_note(texte):
    """Convertit en float, accepte '12,5'. Renvoie None si impossible."""
    try:
        return float(str(texte).replace(",", "."))
    except ValueError:
        return None


def ajouter_etudiant(d, nom, note):
    """Ajoute ou met à jour un étudiant. Renvoie True si OK."""
    valeur = convertir_note(note)
    nom = nom.strip()
    if valeur is None or nom == "":
        return False
    d[nom] = valeur
    return True


def moyenne_classe(d):
    """Moyenne des notes (0.0 si le dictionnaire est vide)."""
    if not d:
        return 0.0
    return sum(d.values()) / len(d)


def meilleur_etudiant(d):
    """Renvoie (nom, note) du meilleur, ou None si vide."""
    if not d:
        return None
    nom = max(d, key=d.get)
    return (nom, d[nom])


def sauvegarder(d, fichier=FICHIER):
    """Écrit 'nom:note' par ligne. Renvoie True si OK."""
    try:
        with open(fichier, "w", encoding="utf-8") as f:
            for nom, note in d.items():
                f.write(f"{nom}:{note}\n")
        return True
    except OSError as e:
        print(f"Erreur d'écriture : {e}")
        return False


def charger(fichier=FICHIER):
    """Lit le fichier et renvoie un dictionnaire (vide si problème)."""
    d = {}
    try:
        with open(fichier, "r", encoding="utf-8") as f:
            for numero, ligne in enumerate(f, start=1):
                ligne = ligne.strip()
                if ligne == "":
                    continue
                nom, _, note = ligne.rpartition(":")
                if nom == "" or not ajouter_etudiant(d, nom, note):
                    print(f"Ligne {numero} ignorée : {ligne!r}")
    except FileNotFoundError:
        print(f"Fichier {fichier} absent : départ avec un dictionnaire vide.")
    except OSError as e:
        print(f"Erreur de lecture : {e}")
    return d


if __name__ == "__main__":
    # Jeu d'essai du prof
    d = {}
    ajouter_etudiant(d, "Alice", 12)
    ajouter_etudiant(d, "Bob", 15)
    ajouter_etudiant(d, "Claire", 9.5)

    print(d)
    print(f"Moyenne : {moyenne_classe(d):.2f}")   # 12.17
    print(meilleur_etudiant(d))                    # ('Bob', 15.0)

    # Sauvegarde puis rechargement
    sauvegarder(d)
    print(charger())

    # Cas limites : aucun ne doit planter
    print(moyenne_classe({}))                      # 0.0
    print(meilleur_etudiant({}))                   # None
    print(ajouter_etudiant(d, "Dave", "abc"))      # False
    print(charger("inexistant.txt"))               # {}