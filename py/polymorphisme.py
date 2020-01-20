class Courrier:

    def __init__(self,poids,mode,adresse_destination,adresse_expedition):
        self.adresse_destination=adresse_destination
        self.adresse_expedition=adresse_expedition
        self.poids=poids
        self.mode=mode

    def toString(self):

        print("Adresse de destination: %s \n Adresse d'expedition: %s\n Poids: %.2f grammes\n Mode de livraison: %s "%(self.adresse_destination,self.adresse_expedition,self.poids,self.mode))

class Lettre(Courrier):

    def __init__(self,poids,mode,adresse_destination,adresse_expedition,format):

        Courrier.__init__(self,poids,mode,adresse_destination,adresse_expedition)
        self.format=format

    def calculTimbre(self):

        if self.format=="A4":tarif_base=2.5
        if self.format=="A3":tarif_base=3.5

        montant=tarif_base*self.poids/1000

        if self.mode=="express":montant*=2

        return montant

    def toString(self):

        print("Lettre:")
        Courrier.toString(self)
        print(" Format:%s\n Prix du timbre:%.2f"%(self.format,self.calculTimbre()))

class Colis(Courrier):
    def __init__(self,poids,mode,adresse_destination,adresse_expedition,volume):
        Courrier.__init__(self,poids,mode,adresse_destination,adresse_expedition)
        self.volume=volume
    def calculTimbre(self):

        montant=0.0

        montant=0.25*self.volume*self.poids/1000

        if self.mode=="express":montant*=2

        return montant

    def toString(self):

        print("Colis:")
        Courrier.toString(self)
        print(" Volume: %.2f litres\n Prix du timbre:%.2f"%(self.volume,self.calculTimbre()))

print('\n')
Lettre=Lettre(80,'normal','MELTDOWN AVENUE','OTAKU SOCIAL CLUB BOULEVARD','A4')
Lettre.toString()
print('\n')
Colis=Colis(3500,'express','OTAKU SOCIAL CLUB BOULEVARD','MELTDOWN AVENUE',2.25)
Colis.toString()
