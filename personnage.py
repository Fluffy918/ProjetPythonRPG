from creature import *

class Personnage(Creature):
    def __init__(self, nom, pv, pm, atck, deff):
        super().__init__(nom, pv, pm, atck, deff)
        self.inventaire = [] # Liste d'objets
        self.niveau = 1
        self.xp = 0
        self.xp_niveau_suivant = 100
    
    def utiliser_objet(self, objet):
        """Utilise un objet de l'inventaire."""
        if objet in self.inventaire:
            print(f"{self.nom} utilise {objet} !")
            if objet == "Potion":
                self.pv += 20
                print(f"{self.nom} récupère 20 pv")
            self.inventaire.remove(objet)
        else:
            print(f"{objet} n'est pas dans l'inventaire")


    def ajouter_objet(self, objet):
        """Ajouter un objet à l'inventaire."""
        self.inventaire.append(objet)
        print(f"{objet} ajouté à l'inventaire de {self.nom}.")

    def gagner_exp(self, montant):
        """Ajouter de l'XP et vérifie si le personnage monte de niveau""" 
        self.xp += montant
        print(f"{self.nom} gagne {montant} XP !")
        if self.xp >= self.xp_niveau_suivant:
            self.niveau += 1
            self.xp -= self.xp_niveau_suivant
            self.xp_niveau_suivant += 50 # Augmentation du seuil pour le niveau suivant
            self.pv += 10 
            self.pm += 5
            self.atck += 2
            self.deff += 2
            print(f"{self.nom} monte au niveau {self.niveau} ! Stats améliorées !")     
