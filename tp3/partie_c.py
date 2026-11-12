import csv
import os

from partie_a import Livre, Utilisateur
from partie_b import Bibliotheque

DOSSIER = os.path.dirname(os.path.abspath(__file__))
FICHIER_LIVRES = os.path.join(DOSSIER, "livres.csv")
CHAMPS = ["titre", "auteur", "annee", "disponible", "emprunteur"]


def sauvegarder(bib, chemin=FICHIER_LIVRES):
    """Écrit les livres au format CSV."""
    with open(chemin, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(CHAMPS)
        for l in bib.livres.values():
            w.writerow([l.titre, l.auteur, l.annee, int(l.disponible),
                        l.emprunteur or ""])


def charger(bib, chemin=FICHIER_LIVRES):
    """Charge les livres dans bib. Fichier absent ou ligne invalide : ignoré.

    Les emprunteurs sont recréés comme utilisateurs si besoin, pour qu'ils
    puissent rendre leurs livres. Renvoie le nombre de livres chargés."""
    if not os.path.exists(chemin):
        return 0
    charges = 0
    with open(chemin, newline="", encoding="utf-8") as f:
        for ligne in csv.DictReader(f):
            try:
                livre = Livre(ligne["titre"], ligne["auteur"], int(ligne["annee"]))
                emprunteur = (ligne["emprunteur"] or "").strip()
                disponible = ligne["disponible"].strip() == "1"
            except (KeyError, ValueError, AttributeError):
                print(f"Ligne ignorée : {ligne}")
                continue
            if not bib.ajouter_livre(livre):
                continue
            charges += 1
            if not disponible and emprunteur:
                if emprunteur not in bib.utilisateurs:
                    bib.ajouter_utilisateur(Utilisateur(emprunteur))
                bib.utilisateurs[emprunteur].emprunter_livre(livre)
    return charges


if __name__ == "__main__":
    b = Bibliotheque()
    b.ajouter_livre(Livre("1984", "Orwell", 1949))
    b.ajouter_utilisateur(Utilisateur("Ana"))
    b.emprunter("Ana", "1984")
    sauvegarder(b)
    b2 = Bibliotheque()
    charger(b2)
    b2.afficher_livres()
    print(b2.rendre("Ana", "1984"))
