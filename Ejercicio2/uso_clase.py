class Municipio:
    # Se declaran atributos de la clase:
    nom = ""
    cve = ""
    __pobTot = 0 #Doble guión bajo son atributos privados.
    _alt = 0     #Un guión bajo son atributos protegidos(solo puede ser utilizada dentro la clase).
    sup = 0
    # Definir constructor:
    def __init__(self, nombre, clave, pobTotal, altitud, superficie): #Aquí se deben declarar todas las variables que se definieron en la clase.
        self.nom = nombre
        self.cve = clave
        self.__pobTot = pobTotal
        self._alt = altitud
        self.sup = superficie
        
    # A todo atributo que sea privado o protegido se le deberá asignar un método GET(solo puede obtenerse) y SET(solo puede asignarse).
    def getNom(self):
        return self.nom
    def setNom(self, nombre):
        try:
            nom = str(nombre)
            self.nom = nombre
        except:
            print("Introduce un municipio: ")

# Se cre la primer instancia:
Mun = Municipio("Toluca", "106", 215425, 4700, 453634)
print(Mun.getNom()) # Aquí se manda llamar los métods que se declararon anteriormente.
