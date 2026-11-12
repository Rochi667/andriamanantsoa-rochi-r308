import os

from partie_a import Livre, Utilisateur
from partie_b import Bibliotheque
from partie_c import charger, sauvegarder

DOSSIER = os.path.dirname(os.path.abspath(__file__))

MENU = """
=== Bibliothèque ===
1 Ajouter un livre
2 Ajouter un utilisateur
3 Emprunter un livre
4 Rendre un livre
5 Afficher les livres
6 Quitter et sauvegarder
7 Statistiques
8 Rechercher par auteur
9 Exporter en JSON"""


def lire_annee():
    while True:
        saisie = input("Année : ").strip()
        try:
            return int(saisie)
        except ValueError:
            print("L'année doit être un nombre.")


def action_ajouter_livre(bib):
    titre = input("Titre : ").strip()
    auteur = input("Auteur : ").strip()
    if not titre or not auteur:
        print("Titre et auteur obligatoires.")
        return
    annee = lire_annee()
    if bib.ajouter_livre(Livre(titre, auteur, annee)):
        print("Livre ajouté.")
    else:
        print("Ce titre existe déjà.")


def action_ajouter_utilisateur(bib):
    nom = input("Nom : ").strip()
    if not nom:
        print("Nom obligatoire.")
    elif bib.ajouter_utilisateur(Utilisateur(nom)):
        print("Utilisateur ajouté.")
    else:
        print("Ce nom existe déjà.")


def action_emprunter(bib):
    nom = input("Nom : ").strip()
    titre = input("Titre : ").strip()
    print("Emprunt enregistré." if bib.emprunter(nom, titre)
          else "Échec : nom ou titre inconnu, livre déjà emprunté ou limite atteinte.")


def action_rendre(bib):
    nom = input("Nom : ").strip()
    titre = input("Titre : ").strip()
    print("Livre rendu." if bib.rendre(nom, titre)
          else "Échec : nom ou titre inconnu, ou livre non emprunté par cette personne.")


def action_stats(bib):
    s = bib.stats()
    print(f"{s['total']} livres, {s['empruntes']} empruntés")
    for nom, n in s["par_utilisateur"].items():
        print(f"  {nom} : {n}")


def action_recherche(bib):
    auteur = input("Auteur : ").strip()
    trouves = bib.rechercher_par_auteur(auteur)
    if not trouves:
        print("Aucun livre trouvé.")
    for livre in trouves:
        livre.afficher()


def action_export(bib):
    chemin = os.path.join(DOSSIER, "livres.json")
    bib.exporter_json(chemin)
    print(f"Export écrit dans {chemin}")


ACTIONS = {
    "1": action_ajouter_livre,
    "2": action_ajouter_utilisateur,
    "3": action_emprunter,
    "4": action_rendre,
    "5": lambda bib: bib.afficher_livres(),
    "7": action_stats,
    "8": action_recherche,
    "9": action_export,
}


def main():
    bib = Bibliotheque()
    n = charger(bib)
    print(f"{n} livre(s) chargé(s)." if n else "Aucune donnée existante, démarrage à vide.")
    while True:
        print(MENU)
        choix = input("Choix : ").strip()
        if choix == "6":
            sauvegarder(bib)
            print("Données sauvegardées. Au revoir !")
            break
        action = ACTIONS.get(choix)
        if action is None:
            print("Choix invalide.")
        else:
            action(bib)


if __name__ == "__main__":
    main()
