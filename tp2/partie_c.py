from partie_a import Grille
from partie_b import JoueurHumain, JoueurIA


def jouer_partie(joueur_x, joueur_o, afficher=True):
    """Fait jouer deux joueurs. Renvoie 'X', 'O' ou None (match nul)."""
    g = Grille()
    joueurs = [joueur_x, joueur_o]
    tour = 0
    while True:
        joueur = joueurs[tour % 2]
        if afficher:
            print()
            g.afficher()
        x, y = joueur.prochain_coup(g, joueur.symbole)
        if not g.jouer(x, y, joueur.symbole):
            continue  # coup invalide : le même joueur rejoue
        if g.est_gagnant(joueur.symbole):
            if afficher:
                print()
                g.afficher()
                print(f"Victoire de {joueur.symbole} !")
            return joueur.symbole
        if g.est_plein():
            if afficher:
                print()
                g.afficher()
                print("Match nul.")
            return None
        tour += 1


def choisir_joueur(symbole, humain):
    return JoueurHumain(symbole) if humain else JoueurIA(symbole)


def main():
    scores = {"X": 0, "O": 0, "nul": 0}
    mode = input("Mode : 1 = contre l'IA, 2 = deux humains : ").strip()
    deux = mode == "2"
    while True:
        gagnant = jouer_partie(JoueurHumain("X"), choisir_joueur("O", deux))
        scores[gagnant or "nul"] += 1
        print(f"Score -> X : {scores['X']} | O : {scores['O']} | nuls : {scores['nul']}")
        if input("Rejouer ? (o/n) : ").strip().lower() != "o":
            break


if __name__ == "__main__":
    main()
