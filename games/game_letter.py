import random

def play_game():
    score_total = 0

    while True:  # Ajout d'une boucle infinie pour permettre de rejouer
        lettre_a_deviner = random.choice("abcdefghijklmnopqrstuvwxyz")
        essais_restants = 3
        score_partie = 0

        while essais_restants > 0:
            print(f"\n** Devine la Lettre **")
            print(f"Essais restants : {essais_restants}")
            supposition = input("Devinez une lettre : ").lower()

            if len(supposition) != 1 or supposition not in "abcdefghijklmnopqrstuvwxyz":
                print("Veuillez entrer une seule lettre valide.")
                continue

            if supposition == lettre_a_deviner:
                print(f"Félicitations, vous avez deviné la lettre : {lettre_a_deviner} !")
                score_partie += 1
                break
            else:
                print("Mauvaise supposition.")
                essais_restants -= 1

        if essais_restants == 0:
            print(f"Désolé, vous avez épuisé tous vos essais. La lettre était : {lettre_a_deviner}")

        score_total += score_partie
        print(f"Score de la partie : {score_partie}")

        reponse = input("Voulez-vous continuer à jouer (c) ou quitter le jeu (q) ? ").lower()
        if reponse == "q":
            return score_total

    return score_total
