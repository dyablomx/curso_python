class vehiculos():
    def __init__(self, marca, modelo):
        self.marca=marca
        self.modelo=modelo
        self.enMarcha=False
        self.acelera=False
        self.frena=False

    def arranca(self):
        self.enMarcha=True

    def acelerar(self):
        self.arranca=True

    def frenar(self):
        self.frena=True

    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo,
              "\nEn Marcha: ", self.enMarcha, "\nAcelerando: ", self.acelera,
              "\nFrenando: ", self.frena)

class Furgoneta(vehiculos):
    def carga(self, cargar):
        self.cargado=cargar
        if (self.cargado):
            print("Furgoneta cargada")
        else:
            print("La furgoneta no esta cargada")

class Moto(vehiculos):
    hcaballito=""
    def caballito(self):
        self.hcaballito="Voy haciendo el caballito"

    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo,
              "\nEn Marcha: ", self.enMarcha, "\nAcelerando: ", self.acelera,
              "\nFrenando: ", self.frena, "\n", self.hcaballito)
        
class VElectricos(vehiculos):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
        self.autonomia=100

    def cargaEnergia(self):
        self.cargando=True


#miMoto=Moto("Honda","CBR")
#miMoto.caballito()
#miMoto.estado()
#miFurgoneta=Furgoneta("Renault","kangoo")
#miFurgoneta.arranca()
#miFurgoneta.estado()
#print(miFurgoneta.carga(True))
#class BicicletaElectrica(VElectricos,vehiculos):
#    pass
#mibici = BicicletaElectrica("Orbea","HJ1500")