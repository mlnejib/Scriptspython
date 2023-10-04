class vehicule:
    def __init__(self,type,energie):
        self.type= type
        self.energie=energie

v1=vehicule("renault","essence")

print(v1.type,v1.energie)
class voiture (vehicule):
    def __init__(self,type,energie,marque):
        self.marque=marque