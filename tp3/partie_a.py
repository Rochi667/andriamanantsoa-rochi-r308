class Livre:
    """Un livre de la bibliothèque."""

    def __init__(self, titre, auteur, annee):
        self.titre = titre
        self.auteur = auteur
        self.annee = annee
        self.disponible = True
        self.emprunteur = None  # nom de l'emprunteur, None si disponible

    def afficher(self):
        etat = "disponible" if self.disponible else f"emprunté par {self.emprunteur}"
        print(f"{self.titre} - {self.auteur} ({self.annee}) [{etat}]")

    def emprunter(self, nom=None):
        """True si le livre était disponible (il est alors emprunté)."""
        if not self.disponible:
            return False
        self.disponible = False
        self.emprunteur = nom
        return True

    def rendre(self):
        """True si le livre était emprunté (il est alors rendu)."""
        if self.disponible:
            return False
        self.disponible = True
        self.emprunteur = None
        return True


class Utilisateur:
    """Un utilisateur et la liste de ses emprunts."""

    LIMITE_EMPRUNTS = 3

    def __init__(self, nom):
        self.nom = nom
        self.emprunts = []  # liste de Livre

    def emprunter_livre(self, livre):
        if livre.emprunter(self.nom):
            self.emprunts.append(livre)
            return True
        return False

    def rendre_livre(self, livre):
        """Refuse si le livre n'a pas été emprunté par cet utilisateur."""
        if livre not in self.emprunts:
            return False
        livre.rendre()
        self.emprunts.remove(livre)
        return True

    def afficher_emprunts(self):
        if not self.emprunts:
            print(f"{self.nom} n'a aucun emprunt.")
            return
        print(f"Emprunts de {self.nom} :")
        for livre in self.emprunts:
            print(f"  - {livre.titre}")


if __name__ == "__main__":
    l = Livre("1984", "Orwell", 1949)
    print(l.emprunter("Ana"))
    print(l.emprunter("Léo"))
    print(l.rendre())
