class Lote:
    def __init__(self, largo, ancho, constructora):
        self.largo = largo
        self.ancho = ancho
        self.constructora = constructora 
        
    def calculararea(self):
        print (self.largo * self.ancho)

    def printconstructora(self):
        print(self.constructora)



class Casa(Lote):
    def __init__(self, largo, ancho, constructora,propietario,telefono):
        super().__init__(largo, ancho, constructora)
        self.propietario = propietario
        self.telefono = telefono
        
        
    def printpropietario(self):
        print(self.propietario)
             
    




x = Casa(7,45,  "yajaira rodriguez","3145925106","Daniel")
x.calculararea()
x.printconstructora()
x.printpropietario()