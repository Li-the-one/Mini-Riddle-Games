import random

def play_game():
    score_total = 0
    essais_par_partie = 7

    while True:  # Ajout d'une boucle infinie pour permettre de rejouer
        nombre_a_deviner = random.randint(1, 100)
        essais_restants = essais_par_partie
        score_partie = 0

        print("\n** Devine le Nombre **")

        while essais_restants > 0:
            print(f"Essais restants : {essais_restants}")
            supposition = input("Devinez un nombre entre 1 et 100 : ")

            if not supposition.isdigit() or not 1 <= int(supposition) <= 100:
                print("Veuillez entrer un nombre valide entre 1 et 100.")
                continue

            supposition = int(supposition)

            if supposition == nombre_a_deviner:
                print(f"Félicitations, vous avez deviné le nombre : {nombre_a_deviner} !")
                score_partie += 1
                break
            elif supposition < nombre_a_deviner:
                print("Le nombre est plus grand. Essayez encore.")
            else:
                print("Le nombre est plus petit. Essayez encore.")

            essais_restants -= 1

        if essais_restants == 0:
            print(f"Désolé, vous avez épuisé tous vos essais. Le nombre était : {nombre_a_deviner}")

        score_total += score_partie
        print(f"Score de la partie : {score_partie}")

        reponse = input("Voulez-vous continuer à jouer (c) ou quitter le jeu (q) ? ").lower()
        if reponse == "q":
            return score_total

    return score_total
