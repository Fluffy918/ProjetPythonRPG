from creature import *
from personnage import *
from monster import *

# Test du système
if __name__ == "__main__":
    # Création du héros et d'un monstre
    hero = Personnage("Tommy", 100, 30, 15, 10)
    aquapode = Monster("aquapode", 50, 10, 8, 5) 

    # Afficher les stats
    hero.afficher_stats()
    aquapode.afficher_stats()

    # Combat
    hero.attaquer(aquapode)
    aquapode.lancer_sort(hero, cout_pm=5, degats=12)

    # Gestion de l'inventaire 
    hero.ajouter_objet("Potion")
    hero.utiliser_objet("Potion")

    # Gagner de l'XP et monter de niveau
    hero.gagner_exp(120)