import os

from partie_c import masque
from partie_d import (DOSSIER, charger_scores, dessin, reveler,
                      sans_accent)

assert masque("PYTHON") == ["_"] * 6
assert sans_accent("É") == "E"
assert sans_accent("A") == "A"

cache = masque("ÉLÉPHANT")
assert reveler("ÉLÉPHANT", "E", cache) is True
assert cache[0] == "É" and cache[2] == "É"
assert reveler("ÉLÉPHANT", "Z", cache) is False

assert "O" in dessin(2)
assert "O" not in dessin(1)

assert charger_scores("fichier_absent.txt") == {}

chemin = os.path.join(DOSSIER, "scores_test.txt")
with open(chemin, "w", encoding="utf-8") as f:
    f.write("Ana:2.0\nnimportequoi\nBob:abc\n")
assert charger_scores(chemin) == {"Ana": 2.0}
os.remove(chemin)

print("Tous les tests passent.")