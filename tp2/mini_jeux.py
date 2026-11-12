import random

from partie_a import Grille
from partie_b import JoueurIA
from partie_c import jouer_partie


class JoueurIAMalin(JoueurIA):
    """Gagne si possible, sinon bloque l'adversaire, sinon hasard."""

    def _coup_gagnant(self, tab, symbole):
        for x in range(Grille.TAILLE):
            for y in range(Grille.TAILLE):
                if tab.cases[x][y] == " ":
                    tab.cases[x][y] = symbole
                    gagne = tab.est_gagnant(symbole)
                    tab.cases[x][y] = " "
                    if gagne:
                        return (x, y)
        return None

    def prochain_coup(self, tab, symbole=None):
        symbole = symbole or self.symbole
        adverse = "X" if symbole == "O" else "O"
        return (self._coup_gagnant(tab, symbole)
                or self._coup_gagnant(tab, adverse)
                or super().prochain_coup(tab, symbole))


def grille_depuis(texte):
    """'XX_/_O_/___' -> Grille."""
    g = Grille()
    for i, ligne in enumerate(texte.split("/")):
        for j, c in enumerate(ligne):
            g.cases[i][j] = " " if c == "_" else c
    return g


if __name__ == "__main__":
    malin = JoueurIAMalin("O")
    print(malin.prochain_coup(grille_depuis("XX_/_O_/___")))  # bloque -> (0, 2)
    print(malin.prochain_coup(grille_depuis("OO_/_XX/___")))  # gagne  -> (0, 2)
    # Malin contre hasard : 20 parties
    bilan = {"X": 0, "O": 0, None: 0}
    for _ in range(20):
        bilan[jouer_partie(JoueurIAMalin("X"), JoueurIA("O"), afficher=False)] += 1
    print("Malin (X) contre hasard (O) :", bilan)
