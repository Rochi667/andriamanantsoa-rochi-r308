# TP1 · Gestion de données et mini-jeux

## Avancement

| Partie | Sujet | Statut |
|---|---|---|
| A | Dictionnaire d'étudiants | Terminée |
| B | Devine le nombre (+ bonus) | Terminée |
| C | Manipulation des mots | Terminée |
| D | Jeu du Pendu (+ hall of fame) | Terminée |

## Fichiers

| Fichier | Contenu |
|---|---|
| `partie_a.py` | Dictionnaire d'étudiants, moyenne, meilleur, sauvegarde/chargement |
| `partie_b.py` | Jeu « Devine le nombre » |
| `partie_c.py` | Chargement des mots, choix d'un mot, masque |
| `partie_d.py` | Jeu du Pendu et hall of fame |
| `test_partie_d.py` | Tests automatiques (parties C et D) |
| `etudiants.txt` | Données de la partie A (format `nom:note`) |
| `mots.txt` | Liste de mots du pendu, un par ligne |
| `scores.txt` | Victoires par joueur (généré par le jeu) |

## Partie A · Dictionnaire d'étudiants
- **Structure :** dictionnaire `nom (str) -> note (float)`
- **Fonctions :** `ajouter_etudiant` (ajoute ou met à jour), `moyenne_classe`, `meilleur_etudiant` (renvoie `(nom, note)`)
- **Fichier :** sauvegarde et rechargement au format `nom:note`
- **Cas gérés :** dictionnaire vide, ligne mal formée, fichier absent

**Jeu d'essai :** Alice 12, Bob 15, Claire 9.5 → moyenne `12.17`, meilleur `('Bob', 15.0)`

**Lancer :** `python tp1/partie_a.py`

## Partie B · Devine le nombre
- Nombre secret tiré avec `random.randint`, 10 essais maximum
- Une saisie invalide (vide ou texte) ne consomme pas d'essai
- **Bonus :** rejouer (`o/n`) et bornes personnalisables

**Lancer :** `python tp1/partie_b.py`

## Partie C · Manipulation des mots
- `charger_mots` lit `mots.txt` en UTF-8 (liste par défaut si le fichier est absent ou vide)
- `choisir_mot(liste)` renvoie un mot en MAJUSCULES
- `masque("PYTHON")` renvoie `['_', '_', '_', '_', '_', '_']`

**Lancer :** `python tp1/partie_c.py`

## Partie D · Jeu du Pendu
- 7 erreurs maximum, ASCII art qui se construit à chaque erreur
- Lettre déjà proposée : pas d'erreur de plus
- Accents gérés : `e` trouve `É` (ÉLÉPHANT), `Python` devient `PYTHON`
- **Hall of fame :** `scores.txt` au format `nom:victoires`, relu au lancement
- **Sécurité :** saisies validées, nom nettoyé, lignes de scores invalides ignorées,
  écriture atomique du fichier, sauvegarde même après `Ctrl + C`

**Lancer :** `python tp1/partie_d.py`
**Tests :** `python tp1/test_partie_d.py`

## Ce que j'ai appris
- **Dictionnaire :** données rangées par clé unique, `.items()` parcourt les paires
- **`input()` et `int()` :** `input()` renvoie toujours du texte, `int()` le convertit
- **`try / except` :** gérer une erreur au lieu de laisser le programme planter
- **Fonctions :** `def`, paramètres, `return`, pour ne pas répéter le code
- **Modules :** `import` pour réutiliser les fonctions d'un autre fichier
- **Fichiers :** `with open(...)`, encodage UTF-8, écriture atomique
- **Tests :** `assert` pour vérifier le code sans jouer à la main
- **Git :** un commit par partie, `git add`, `git commit`, `git push`

## Difficultés rencontrées
- `ValueError` sur une saisie vide : réglé avec `try / except`
- Dossiers `tp1` imbriqués et nom en majuscules : réorganisés, GitHub distingue `TP1` et `tp1`
- Commandes cmd lancées dans PowerShell (`type nul`) : remplacées par `ni`
- Commits signés « unknown » : corrigé avec `git config --global`