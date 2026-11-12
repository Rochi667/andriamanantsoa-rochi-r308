# TP2 · POO et jeu du Morpion

## Avancement

| Partie | Sujet | Statut |
|---|---|---|
| A | Classe `Grille` | Terminée |
| B | Classes `JoueurHumain` et `JoueurIA` | Terminée |
| C | Jeu complet (score multi-parties, mode 2 humains) | Terminée |
| Mini-jeux | `JoueurIAMalin` | Terminé |

## Fichiers

| Fichier | Contenu |
|---|---|
| `partie_a.py` | `Grille` : `afficher`, `jouer`, `est_gagnant`, `est_plein` |
| `partie_b.py` | `JoueurHumain` (clavier) et `JoueurIA` (hasard), méthode `prochain_coup(tab, symbole)` |
| `partie_c.py` | Boucle de jeu, scores, mode 2 humains |
| `mini_jeux.py` | `JoueurIAMalin` : gagne, sinon bloque, sinon hasard |
| `test_tp2.py` | Tests automatiques |

## Lancer
```bash
cd tp2
python partie_c.py     # jouer
python mini_jeux.py    # IA qui bloque, malin contre hasard
python test_tp2.py     # tests
```
Un coup invalide (case occupée, hors grille, saisie illisible) fait rejouer le même joueur.
