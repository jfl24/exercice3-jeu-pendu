import random

mots = ["python", "programmation", "github", "collaboration", "projet", "automne"]
def choisir_mot():
    secret = random.randint(1, len(mots) - 1)
    mot_secret = mots[secret]
    return mot_secret






