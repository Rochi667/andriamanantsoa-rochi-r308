# TP1 · Gestion de données et mini-jeux

## Avancement

| Partie | Sujet | Statut |
|---|---|---|
| A | Dictionnaire d'étudiants | Terminée |
| B | Devine le nombre (+ bonus) | Terminée |
| C | Manipulation des mots | À faire |
| D | Jeu du Pendu | À faire |

## Fichiers

| Fichier | Contenu |
|---|---|
| `partie_a.py` | Dictionnaire d'étudiants, moyenne, meilleur, sauvegarde/chargement |
| `partie_b.py` | Jeu « Devine le nombre » |
| `etudiants.txt` | Données sauvegardées (format `nom:note`) |

## Partie A · Dictionnaire d'étudiants
- **Structure :** dictionnaire `nom (str) -> note (float)`
- **Fonctions :** `ajouter_etudiant` (ajoute ou met à jour), `moyenne_classe`, `meilleur_etudiant` (renvoie `(nom, note)`)
- **Fichier :** sauvegarde et rechargement au format `nom:note`, une ligne par étudiant
- **Cas gérés :** dictionnaire vide, ligne mal formée, fichier absent (départ avec un dictionnaire vide)

**Jeu d'essai :** Alice 12, Bob 15, Claire 9.5 → moyenne `12.17`, meilleur `('Bob', 15.0)`

**Lancer :** `python tp1/partie_a.py`

## Partie B · Devine le nombre
- Nombre secret tiré avec `random.randint`, 10 essais maximum
- Messages : « Trop petit », « Trop grand », « Gagné »
- Une saisie invalide (vide ou texte) ne consomme pas d'essai
- **Bonus :** rejouer (`o/n`) et bornes personnalisables

**Lancer :** `python tp1/partie_b.py`

## Ce que j'ai appris
- **Dictionnaire :** les données sont rangées par clé unique, et `.items()` parcourt les paires
- **`input()` et `int()` :** `input()` renvoie toujours du texte, `int()` le convertit
- **`try / except ValueError` :** gérer une erreur au lieu de laisser le programme planter
- **Fonctions :** `def`, paramètres et `return`, pour ne pas répéter le code
- **Boucles :** `for ... in range(...)` quand on connaît le nombre de tours, `while` sinon
- **Modules :** `import random` pour tirer un nombre au hasard
- **Git :** un commit par partie, `git add`, `git commit`, `git push`
- **Recherche dichotomique :** couper l'intervalle en deux résout 1-100 en 7 essais maximum

## Difficultés rencontrées
- `ValueError` quand on appuie sur Entrée sans rien taper : réglé avec `try / except`
- Dossier `TP1/tp1` en trop et nom en majuscules : réorganisé, car GitHub distingue `TP1` et `tp1`
- Commits signés « unknown » : corrigé avec `git config --global user.name` et `user.email`