
import random
from mots import choisir_mot       
from affichage import afficher_pendu  
from jeu import jouer_tour         

def main():
    mot_secret = choisir_mot()
    lettres_trouvees = set()
    erreurs = 0
    max_erreurs = 6

    print("=== JEU DU PENDU ===")

    while erreurs < max_erreurs:
        afficher_pendu(erreurs)

        affichage = "".join(
            lettre if lettre in lettres_trouvees else "_"
            for lettre in mot_secret
        )
        print("Mot :", affichage)

        if "_" not in affichage:
            print("Bravo, tu as gagné !")
            return

        lettre = input("Choisis une lettre : ").lower()

        erreur = jouer_tour(mot_secret, lettres_trouvees, lettre)
        if erreur:
            erreurs += 1

    afficher_pendu(erreurs)
    print("Perdu ! Le mot était :", mot_secret)

if __name__ == "__main__":
    main()
