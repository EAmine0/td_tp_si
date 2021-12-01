import string


class Character:
    nom = None
    prenom = None
    age = None
    profession = None
    boostmoral = None

    def __init__(self, nom, prenom, age, profession, boostmoral):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.profession = profession
        self.boostmoral = boostmoral

    def getNom(self):
        return self.nom

    def getPrenom(self):
        return self.prenom

    def getAge(self):
        return self.age

    def getProfession(self):
        return self.profession

    def getBoostMoral(self):
        return self.boostmoral

    def setNom(self, nom):
        self.nom = nom

    def setPrenom(self, prenom):
        self.prenom = prenom

    def setAge(self, age):
        self.age = age

    def setProfession(self, profession):
        self.profession = profession

    def setBoostMoral(self, boostmoral):
        self.boostmoral = boostmoral

    def __repr__(self):
        return "test"
