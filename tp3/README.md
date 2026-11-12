# TP3 · Gestion d'une bibliothèque

## Avancement

| Partie | Sujet | Statut |
|---|---|---|
| A | Classes `Livre` et `Utilisateur` | Terminée |
| B | `Bibliotheque` | Terminée |
| C | Persistance CSV | Terminée |
| D | Menu interactif | Terminée |
| E | Recherche par auteur, limite d'emprunts, export JSON | Terminée |
| Défi 1 | `stats()` (option 7) | Terminé |
| Défi 2 | Cas piégés sans plantage | Terminé |

## Fichiers

| Fichier | Contenu |
|---|---|
| `partie_a.py` | `Livre`, `Utilisateur` |
| `partie_b.py` | `Bibliotheque` (+ `stats`, `rechercher_par_auteur`, `exporter_json`) |
| `partie_c.py` | `sauvegarder` / `charger` en CSV (`livres.csv`, généré) |
| `partie_d.py` | Programme principal (menu) |
| `test_tp3.py` | Tests automatiques |

## Lancer
```bash
cd tp3
python partie_d.py     # menu interactif
python test_tp3.py     # tests
```
Limite : 3 emprunts par utilisateur. Un livre ne peut être rendu que par son emprunteur.
