import json

from partie_a import Livre, Utilisateur


class Bibliotheque:
    """Gestionnaire : livres (titre -> Livre), utilisateurs (nom -> Utilisateur)."""

    def __init__(self):
        self.livres = {}
        self.utilisateurs = {}

    def ajouter_livre(self, livre):
        """False si un livre du même titre existe déjà."""
        if livre.titre in self.livres:
            return False
        self.livres[livre.titre] = livre
        return True

    def ajouter_utilisateur(self, utilisateur):
        """False si le nom est déjà pris."""
        if utilisateur.nom in self.utilisateurs:
            return False
        self.utilisateurs[utilisateur.nom] = utilisateur
        return True

    def emprunter(self, nom, titre):
        """False (sans plantage) si nom ou titre inconnu, ou livre déjà emprunté."""
        user = self.utilisateurs.get(nom)
        livre = self.livres.get(titre)
        if user is None or livre is None:
            return False
        if len(user.emprunts) >= Utilisateur.LIMITE_EMPRUNTS:
            return False
        return user.emprunter_livre(livre)

    def rendre(self, nom, titre):
        user = self.utilisateurs.get(nom)
        livre = self.livres.get(titre)
        if user is None or livre is None:
            return False
        return user.rendre_livre(livre)

    def afficher_livres(self):
        dispo = [l for l in self.livres.values() if l.disponible]
        pris = [l for l in self.livres.values() if not l.disponible]
        print("Livres disponibles :")
        for l in dispo:
            print(f"  - {l.titre} ({l.auteur}, {l.annee})")
        if not dispo:
            print("  (aucun)")
        print("Livres empruntés :")
        for l in pris:
            print(f"  - {l.titre} ({l.auteur}, {l.annee}) par {l.emprunteur}")
        if not pris:
            print("  (aucun)")

    def stats(self):
        """Nombre de livres, d'emprunts et emprunts par utilisateur."""
        par_user = {nom: len(u.emprunts) for nom, u in self.utilisateurs.items()
                    if u.emprunts}
        return {"total": len(self.livres),
                "empruntes": sum(1 for l in self.livres.values() if not l.disponible),
                "par_utilisateur": par_user}

    def rechercher_par_auteur(self, auteur):
        """Livres dont l'auteur contient le texte (sans tenir compte de la casse)."""
        auteur = auteur.strip().lower()
        return [l for l in self.livres.values() if auteur and auteur in l.auteur.lower()]

    def exporter_json(self, chemin):
        donnees = [{"titre": l.titre, "auteur": l.auteur, "annee": l.annee,
                    "disponible": l.disponible, "emprunteur": l.emprunteur}
                   for l in self.livres.values()]
        with open(chemin, "w", encoding="utf-8") as f:
            json.dump(donnees, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    b = Bibliotheque()
    b.ajouter_livre(Livre("1984", "Orwell", 1949))
    b.ajouter_utilisateur(Utilisateur("Ana"))
    print(b.emprunter("Ana", "1984"))
    print(b.emprunter("Ana", "1984"))
    print(b.emprunter("Zoé", "1984"))
    print(b.emprunter("Ana", "Inconnu"))
    b.afficher_livres()
