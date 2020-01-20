class DateNaissance:

    def __init__(self, jour, mois, annee):

        self.jour=jour
        self.mois=mois
        self.annee=annee

    def toString(self):

        return "%02d / %02d / %d" %(self.jour,self.mois,self.annee)

class Personne:

    def __init__(self, nom, prenom, ville,date_de_naissance):

        self.nom=nom
        self.prenom=prenom
        self.date_de_naissance=date_de_naissance
        self.ville=ville

    def afficher(self):

        print("%s %s née le %s à %s"%(self.nom,self.prenom,self.ville,self.date_de_naissance.toString()))

class Employe(Personne):

    def __init__(self, nom,prenom,ville,date_naissance,salaire):
        Personne.__init__(self,nom,prenom,ville,date_naissance)
        self.salaire=salaire
    def afficher(self):
        Personne.afficher(self)
        print("Salaire: %.02f"%self.salaire)

class Chef(Employe):

    def __init__(self,nom,prenom,ville,date_naissance,salaire,service):
        Employe.__init__(self,nom,prenom,ville,date_naissance,salaire)
        self.service=service
    def afficher(self):
        Employe.afficher(self)
        print("Service : %s"%self.service)


print('\n')
Test1=Personne('Jean','de La Fontaine', 'Château-Thierry',DateNaissance(8,7,1621))
Test1.afficher()
print('\n')
Test2=Employe('Jean','de La Fontaine', 'Château-Thierry', DateNaissance(8,7,1621), 2559.59)
Test2.afficher()
print('\n')
Test3=Chef('Jean','de La Fontaine', 'Château-Thierry', DateNaissance(8,7,1621), 2559.59,'Fable & Poésie')
Test3.afficher()
