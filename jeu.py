def jouer_tour(mot_secret, lettres_trouvees, lettre):
    # verifie si la lettre est déjà essayée
    if lettre in lettres_trouvees:
        return False, "Lettre déjà utilisée"

    # ajouter la lettre à la liste
    lettres_trouvees.append(lettre)

    # vérifier si la lettre est dans le mot secret
    if lettre in mot_secret:
        message = "Bonne lettre !"
        trouve = True
    else:
        message = "Mauvaise lettre..."
        trouve = False

    return trouve, message
