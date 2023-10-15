import random
import categories.animals as animals
import categories.countries as countries
import categories.food as food
import categories.sports as sports
import categories.couleurs as couleurs
def play_game():
    score_total = 0

    while True:  # Ajout d'une boucle infinie pour permettre de rejouer
        categories_mots = {
            "Animaux": animals.animals_words,
            "Pays": countries.countries_words,
            "Nourriture": food.food_words,
            "Sports" : sports.sports_words,
            "Couleurs" : couleurs.colors_words
        }

        # Sélectionnez une catégorie
        print("Catégories de mots disponibles :")
        for categorie in categories_mots.keys():
            print(f"- {categorie}")

        categorie = input("Choisissez une catégorie : ").capitalize()

        mots_de_la_categorie = categories_mots.get(categorie)
        if mots_de_la_categorie is None:
            print(f"Catégorie invalide : {categorie}")
            continue

        mot_a_deviner = random.choice(mots_de_la_categorie).lower()
        lettres_devinees = set()
        essais_restants = 6
        score_partie = 0

        while essais_restants > 0:
            mot_affiche = ""

            for lettre in mot_a_deviner:
                if lettre in lettres_devinees:
                    mot_affiche += lettre
                else:
                    mot_affiche += "_"

            print(f"\n** Devine le Mot de la catégorie '{categorie}' **")
            print("Mot à deviner :", mot_affiche)
            print("Lettres déjà devinées :", " ".join(lettres_devinees))
            print(f"Essais restants : {essais_restants}")

            if mot_a_deviner == mot_affiche:
                print(f"Félicitations, vous avez deviné le mot : {mot_a_deviner} !")
                score_partie += 1
                break

            supposition = input("Devinez une lettre : ").lower()

            if len(supposition) != 1 or supposition not in "abcdefghijklmnopqrstuvwxyz":
                print("Veuillez entrer une seule lettre valide.")
                continue

            if supposition in lettres_devinees:
                print("Vous avez déjà deviné cette lettre.")
            else:
                lettres_devinees.add(supposition)
                if supposition in mot_a_deviner:
                    print("Bonne supposition !")
                else:
                    print("Mauvaise supposition.")
                essais_restants -= 1

        if essais_restants == 0:
            print(f"Désolé, vous avez épuisé tous vos essais. Le mot était : {mot_a_deviner}")

        score_total += score_partie
        print(f"Score de la partie : {score_partie}")

        reponse = input("Voulez-vous continuer à jouer (c) ou quitter le jeu (q) ? ").lower()
        if reponse == "q":
            return score_total

    return score_total
