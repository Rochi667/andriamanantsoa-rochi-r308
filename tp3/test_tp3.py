import os
import tempfile
import unittest

from partie_a import Livre, Utilisateur
from partie_b import Bibliotheque
from partie_c import charger, sauvegarder


def biblio():
    b = Bibliotheque()
    b.ajouter_livre(Livre("1984", "Orwell", 1949))
    b.ajouter_livre(Livre("Dune", "Herbert", 1965))
    b.ajouter_livre(Livre("La Ferme", "Orwell", 1945))
    b.ajouter_utilisateur(Utilisateur("Ana"))
    b.ajouter_utilisateur(Utilisateur("Léo"))
    return b


class TestLivre(unittest.TestCase):
    def test_emprunt_rendu(self):
        l = Livre("1984", "Orwell", 1949)
        self.assertTrue(l.emprunter("Ana"))
        self.assertFalse(l.emprunter("Léo"))
        self.assertTrue(l.rendre())
        self.assertFalse(l.rendre())


class TestBibliotheque(unittest.TestCase):
    def test_cas_pieges(self):
        b = biblio()
        self.assertFalse(b.emprunter("Inconnu", "1984"))
        self.assertFalse(b.emprunter("Ana", "Inconnu"))
        self.assertTrue(b.emprunter("Ana", "1984"))
        self.assertFalse(b.emprunter("Léo", "1984"))
        self.assertFalse(b.rendre("Léo", "1984"))  # pas l'emprunteur
        self.assertTrue(b.rendre("Ana", "1984"))

    def test_stats(self):
        b = biblio()
        b.emprunter("Ana", "1984")
        b.emprunter("Ana", "Dune")
        self.assertEqual(b.stats(),
                         {"total": 3, "empruntes": 2, "par_utilisateur": {"Ana": 2}})

    def test_limite_et_recherche(self):
        b = biblio()
        b.ajouter_livre(Livre("Fondation", "Asimov", 1951))
        for t in ("1984", "Dune", "La Ferme"):
            self.assertTrue(b.emprunter("Ana", t))
        self.assertFalse(b.emprunter("Ana", "Fondation"))
        self.assertEqual(len(b.rechercher_par_auteur("orwell")), 2)


class TestPersistance(unittest.TestCase):
    def test_sauvegarde_rechargement(self):
        b = biblio()
        b.emprunter("Ana", "1984")
        with tempfile.TemporaryDirectory() as d:
            chemin = os.path.join(d, "livres.csv")
            sauvegarder(b, chemin)
            b2 = Bibliotheque()
            self.assertEqual(charger(b2, chemin), 3)
            self.assertEqual(b2.livres["1984"].emprunteur, "Ana")
            self.assertTrue(b2.rendre("Ana", "1984"))

    def test_fichier_absent(self):
        self.assertEqual(charger(Bibliotheque(), "/inexistant/livres.csv"), 0)


if __name__ == "__main__":
    unittest.main()
