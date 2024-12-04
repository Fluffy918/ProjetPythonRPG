class Creature:
    def __init__(self, nom, pv, pm, atck, deff):
        self.nom = nom
        self.pv = pv
        self.pm = pm
        self.atck = atck
        self.deff = deff

    def attaquer(self, cible):
        """Effectue une attaque sur une cible."""
        degats = max(1, self.atck - cible.deff) # Les dégats ne peuvent pas être supérieur à 1
        cible.pv -= degats
        print(f"{self.nom} attaque {cible.nom} et inflige {degats} dégats !")
        if cible.pv <= 0:
            print(f"{cible.nom} est vaincue(e) !")
    
    def lancer_sort(self, cible, cout_pm, degats):
        """Lance un sort si le personnage a asser de PM."""
        if self.pm >= cout_pm:
            self.pm -= cout_pm
            cible.pv -= degats
            print(f"{self.nom} lance un sort sur {cible.nom} et inflige {degats} dégats !")
            if cible.pv <= 0:
                print(f"{cible.nom} est vaincu(e)")
        else:
            print(f"{self.nom} n'a pas assez de PM")
    
    def afficher_stats(self):
        """Affiche les statistiques actuelles du personnage."""
        print(f"Nom: {self.nom} | PV: {self.pv} | PM: {self.pm} | Atck: {self.atck} | Deff: {self.deff}")





