import random

from partie_a import Grille


class JoueurHumain:
    """Joueur qui saisit son coup au clavier."""

    def __init__(self, symbole):
        self.symbole = symbole

    def prochain_coup(self, tab, symbole=None):
        """Demande 'x y' (0 à 2). Renvoie (x, y). Redemande si illisible."""
        while True:
            saisie = input(f"Joueur {self.symbole} (ligne colonne) : ").split()
            try:
                if len(saisie) != 2:
                    raise ValueError
                return int(saisie[0]), int(saisie[1])
            except ValueError:
                print("Entre deux nombres, par exemple : 1 2")


class JoueurIA:
    """IA qui joue une case libre au hasard."""

    def __init__(self, symbole):
        self.symbole = symbole

    def prochain_coup(self, tab, symbole=None):
        libres = [(x, y) for x in range(Grille.TAILLE)
                  for y in range(Grille.TAILLE) if tab.cases[x][y] == " "]
        return random.choice(libres)


if __name__ == "__main__":
    g = Grille()
    ia = JoueurIA("O")
    print(ia.prochain_coup(g))
