class Grille:
    """Grille de morpion 3x3 (liste de listes)."""

    TAILLE = 3

    def __init__(self):
        self.cases = [[" "] * self.TAILLE for _ in range(self.TAILLE)]

    def afficher(self):
        """Rendu lisible de la grille."""
        lignes = [" " + " | ".join(ligne) + " " for ligne in self.cases]
        print(("\n" + "-" * 9 + "\n").join(lignes))

    def case_libre(self, x, y):
        """True si (x, y) est dans la grille et vide."""
        return (0 <= x < self.TAILLE and 0 <= y < self.TAILLE
                and self.cases[x][y] == " ")

    def jouer(self, x, y, joueur):
        """Place le symbole du joueur si la case est libre. Renvoie True/False."""
        if joueur not in ("X", "O"):
            print("Symbole invalide.")
            return False
        if not (0 <= x < self.TAILLE and 0 <= y < self.TAILLE):
            print("Coup refusé : hors grille.")
            return False
        if self.cases[x][y] != " ":
            print("Coup refusé : case occupée.")
            return False
        self.cases[x][y] = joueur
        return True

    def est_gagnant(self, j):
        """True si le joueur j a une ligne, une colonne ou une diagonale."""
        n = self.TAILLE
        lignes = [list(l) for l in self.cases]
        colonnes = [[self.cases[i][k] for i in range(n)] for k in range(n)]
        diagonales = [[self.cases[i][i] for i in range(n)],
                      [self.cases[i][n - 1 - i] for i in range(n)]]
        return any(all(c == j for c in ligne)
                   for ligne in lignes + colonnes + diagonales)

    def est_plein(self):
        """True si aucune case libre."""
        return all(c != " " for ligne in self.cases for c in ligne)


if __name__ == "__main__":
    g = Grille()
    g.jouer(0, 0, "X")
    g.jouer(0, 1, "O")
    g.jouer(1, 1, "X")
    g.afficher()
    print(g.jouer(0, 0, "O"))
    print(g.jouer(3, 0, "O"))
    print(g.est_gagnant("X"))
    g.jouer(2, 2, "X")
    print(g.est_gagnant("X"))
