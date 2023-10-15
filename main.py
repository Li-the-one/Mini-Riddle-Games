import games.game_word as game_word
import games.game_letter as game_letter
import games.game_number as game_number
import json

# Créez un dictionnaire vide pour stocker les scores
scores = {}

# Créez une fonction pour ajouter le score au dictionnaire
def ajouter_score(joueur, score):
    if joueur in scores:
        scores[joueur] += score
    else:
        scores[joueur] = score

# Créez une fonction pour afficher les 10 meilleurs scores
def afficher_meilleurs_scores():
    print("Meilleurs scores :")
    top_scores = list(scores.items())
    top_scores.sort(key=lambda x: x[1], reverse=True)
    for i, (joueur, score) in enumerate(top_scores[:10], start=1):
        print(f"{i}. {joueur}: {score}")

# Fonction pour sauvegarder les scores dans un fichier JSON
def sauvegarder_scores():
    with open("scores.json", "w") as fichier_scores:
        json.dump(scores, fichier_scores)

# Fonction pour charger les scores depuis un fichier JSON
def charger_scores():
    try:
        with open("scores.json", "r") as fichier_scores:
            scores.update(json.load(fichier_scores))
    except FileNotFoundError:
        pass  # Le fichier n'existe pas encore, pas de scores à charger

def main():
    charger_scores()  # Chargez les scores au début de la session

    score_total = 0
    parties_jouees = 0

    while True:
        print("\nMenu Principal :")
        print("1. Devine un Mot")
        print("2. Devine une Lettre")
        print("3. Devine un Nombre")
        print("4. Classements")
        print("5. Quitter")

        choix = input("Choisissez un jeu (1/2/3) ou accédez aux classements (4) ou quittez (5) : ").lower()

        if choix == "1":
            score_partie = game_word.play_game()
            score_total += score_partie
            ajouter_score("Joueur", score_partie)
        elif choix == "2":
            score_partie = game_letter.play_game()
            score_total += score_partie
            ajouter_score("Joueur", score_partie)
        elif choix == "3":
            score_partie = game_number.play_game()
            score_total += score_partie
            ajouter_score("Joueur", score_partie)
        elif choix == "4":
            afficher_meilleurs_scores()
        elif choix == "5":
            sauvegarder_scores()  # Sauvegardez les scores à la fin de la session
            break  # Quitter le jeu

        parties_jouees += 1

        if parties_jouees >= 3:
            continuer = input("Vous avez joué à 3 parties. Voulez-vous continuer à jouer (o/n) ? : ").lower()
            if continuer != "o":
                sauvegarder_scores()  # Sauvegardez les scores avant de quitter
                break

    print(f"Score total après 3 parties : {score_total}")

if __name__ == "__main__":
    main()
