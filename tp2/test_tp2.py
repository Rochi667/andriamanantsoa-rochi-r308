import io
import unittest
from contextlib import redirect_stdout

from partie_a import Grille
from partie_b import JoueurIA
from partie_c import jouer_partie
from mini_jeux import JoueurIAMalin, grille_depuis


class TestGrille(unittest.TestCase):
    def test_coups_invalides(self):
        g = Grille()
        with redirect_stdout(io.StringIO()):
            self.assertTrue(g.jouer(0, 0, "X"))
            self.assertFalse(g.jouer(0, 0, "O"))
            self.assertFalse(g.jouer(3, 0, "O"))
            self.assertFalse(g.jouer(-1, 0, "O"))

    def test_victoire_diagonale(self):
        g = Grille()
        for i in range(3):
            g.jouer(i, i, "X")
        self.assertTrue(g.est_gagnant("X"))
        self.assertFalse(g.est_gagnant("O"))

    def test_plein(self):
        g = Grille()
        self.assertFalse(g.est_plein())
        for x in range(3):
            for y in range(3):
                g.jouer(x, y, "X")
        self.assertTrue(g.est_plein())


class TestJeu(unittest.TestCase):
    def test_ia_contre_ia(self):
        for _ in range(20):
            r = jouer_partie(JoueurIA("X"), JoueurIA("O"), afficher=False)
            self.assertIn(r, ("X", "O", None))

    def test_ia_malin(self):
        m = JoueurIAMalin("O")
        self.assertEqual(m.prochain_coup(grille_depuis("XX_/_O_/___")), (0, 2))
        self.assertEqual(m.prochain_coup(grille_depuis("OO_/_XX/___")), (0, 2))


if __name__ == "__main__":
    unittest.main()
