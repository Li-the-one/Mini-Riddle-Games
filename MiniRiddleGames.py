import random

# Liste de mots à deviner
mots = ["python", "informatique", "programmation", "challenge", "ordinateur", "apprentissage", "internet", "algorithmes", "developpeur"]

def devine_le_mot():
    mot_a_deviner = random.choice(mots).lower()
    lettres_devinees = []
    essais_restants = 6

    while essais_restants > 0:
        mot_affiche = ""
        lettres_restantes = 0  # Compteur des lettres restantes à deviner

        for lettre in mot_a_deviner:
            if lettre in lettres_devinees:
                mot_affiche += lettre
            else:
                mot_affiche += "_"
                lettres_restantes += 1  # Incrémenter le compteur
        
        print("\n** Devine le Mot **")
        print("Mot à deviner :", mot_affiche)
        print("Lettres déjà devinées :", lettres_devinees)
        print(f"Essais restants : {essais_restants}")
        
        if lettres_restantes == 0:
            print(f"Félicitations, vous avez deviné le mot : {mot_a_deviner} !")
            return True
        
        supposition = input("Devinez une lettre : ").lower()
        
        if len(supposition) != 1 or not supposition.isalpha():
            print("Veuillez entrer une seule lettre valide.")
            continue
        
        if supposition in lettres_devinees:
            print("Vous avez déjà deviné cette lettre.")
        else:
            lettres_devinees.append(supposition)
            if supposition in mot_a_deviner:
                print("Bonne supposition !")
            else:
                print("Mauvaise supposition.")
                essais_restants -= 1
    
    print(f"Désolé, vous avez épuisé tous vos essais. Le mot était : {mot_a_deviner}")
    return False

def devine_le_nombre():
    nombre_a_deviner = random.randint(1, 100)
    essais_restants = 7

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
            return True
        elif supposition < nombre_a_deviner:
            print("Le nombre que vous cherchez est plus grand.")
        else:
            print("Le nombre que vous cherchez est plus petit.")
        
        essais_restants -= 1
    
    print(f"Désolé, vous avez épuisé tous vos essais. Le nombre était : {nombre_a_deviner}")
    return False

def rejouer():
    reponse = input("Voulez-vous rejouer ? (oui/non) : ").lower()
    return reponse == "oui"

def jeu_de_devinette():
    score = 0
    essais = 3

    print("Bienvenue au jeu de devinette ! Vous avez 3 essais pour gagner des points.")
    
    while essais > 0:
        jeu = random.choice([devine_le_mot, devine_le_nombre])
        if jeu():
            score += 1
        print(f"Votre score actuel : {score}")
        essais -= 1

    print(f"Jeu terminé. Votre score final : {score}")
    if rejouer():
        jeu_de_devinette()

if __name__ == "__main__":
    jeu_de_devinette()
