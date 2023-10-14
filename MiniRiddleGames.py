import random

# Dictionnaire de catégories de mots et leurs listes de mots associées
categories_mots = {
    "Animaux": ["chien", "chat", "éléphant", "tigre", "oiseau", "dauphin"],
    "Pays": ["France", "Italie", "Japon", "Canada", "Brésil", "Australie"],
    "Nourriture": ["pizza", "hamburger", "spaghetti", "sushi", "chocolat", "fraise"],
}

lettres = "abcdefghijklmnopqrstuvwxyz"

def devine_un_mot(categorie):
    mots_de_la_categorie = categories_mots.get(categorie)
    if mots_de_la_categorie is None:
        print(f"Catégorie invalide : {categorie}")
        return

    mot_a_deviner = random.choice(mots_de_la_categorie).lower()
    lettres_devinees = set()
    essais_restants = 6

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
            return True
        
        supposition = input("Devinez une lettre : ").lower()
        
        if len(supposition) != 1 or supposition not in lettres:
            print("Veuillez entrer une seule lettre valide.")
            continue
        
        if supposition in lettres_devinees:
            print("Vous avez déjà deviné cette lettre.")
        else:
            lettres_devinees.add(supposition)
            print("Bonne supposition !" if supposition in mot_a_deviner else "Mauvaise supposition.")
            essais_restants -= 1
    
    print(f"Désolé, vous avez épuisé tous vos essais. Le mot était : {mot_a_deviner}")
    return False

def devine_une_lettre():
    lettre_a_deviner = random.choice(lettres)
    lettres_devinees = set()
    essais_restants = 6

    while essais_restants > 0:
        print("\n** Devine la Lettre **")
        print("Lettres déjà devinées :", " ".join(lettres_devinees))
        print(f"Essais restants : {essais_restants}")
        
        if len(lettres_devinees) == 25:
            print(f"Félicitations, vous avez deviné toutes les lettres !")
            return True
        
        supposition = input("Devinez une lettre : ").lower()
        
        if len(supposition) != 1 or supposition not in lettres:
            print("Veuillez entrer une seule lettre valide.")
            continue
        
        if supposition in lettres_devinees:
            print("Vous avez déjà deviné cette lettre.")
        else:
            lettres_devinees.add(supposition)
            print("Bonne supposition !" if supposition == lettre_a_deviner else "Mauvaise supposition.")
            essais_restants -= 1
    
    print(f"Désolé, vous avez épuisé tous vos essais. La lettre était : {lettre_a_deviner}")
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

def affiche_categories():
    print("Catégories de mots disponibles :")
    for categorie in categories_mots.keys():
        print(f"- {categorie}")

def jeu_de_devinette():
    score = 0
    essais = 3

    print("Bienvenue à Mini Riddle Games !")

    while essais > 0:
        print(f"Vous avez {essais} partie(s) restante(s).")
        print("Choisissez un jeu :")
        print("1. Deviner un Mot")
        print("2. Deviner une Lettre")
        print("3. Deviner un Nombre")
        choix = input("Entrez le numéro du jeu : ")

        if choix == "1":
            affiche_categories()
            categorie = input("Choisissez une catégorie : ").capitalize()
            if categorie in categories_mots:
                if devine_un_mot(categorie):
                    score += 1
                print(f"Votre score actuel : {score}")
            else:
                print(f"Catégorie invalide : {categorie}")
        elif choix == "2":
            if devine_une_lettre():
                score += 1
            print(f"Votre score actuel : {score}")
        elif choix == "3":
            if devine_le_nombre():
                score += 1
            print(f"Votre score actuel : {score}")
        else:
            print("Choix de jeu invalide.")
    
    print(f"Jeu terminé. Votre score final : {score}")

if __name__ == "__main__":
    jeu_de_devinette()
