class Municipio:
    # Se declaran atributos de la clase:
    nom = ""
    cve = ""
    __pobTot = 0 # Doble guión bajo son atributos privados.
    _alt = 0     # Un guión bajo son atributos protegidos(solo puede ser utilizada dentro la clase).
    sup = 0
    # Definir constructor:
    def __init__(self, nombre, clave, pobTotal, altitud, superficie): #Aquí se deben declarar todas las variables que se definieron en la clase.
        self.nom = nombre
        self.cve = clave
        self.__pobTot = pobTotal
        self._alt = altitud
        self.sup = superficie
    # A todo atributo que sea privado o protegido se le deberá asignar un método GET y SET
    # Definir los métodos GET y SET
    def getNom(self):
        return self.nom
    def setNom(self, nombre):
        try:
            nom = str(nombre)
            self.nom = nombre
        except:
            print("Introduce un municipio: ")
    def getCve(self):
        return self.cve
    def setCve(self, clave):
        self.cve = clave
    def getPobTot(self):
        return self.__pobTot
    def setPobTot(self, pobTotal):
        self.__pobTot = pobTotal
    def getAlt(self):
        return self._alt
    def setAlt(self, altitud):
        self._alt = altitud
    def getSup(self):
        return self.sup
    def setSup(self, superficie):
        self.sup = superficie
    
    # Después de asignar los GET y SET
    # Se escriben los métodos que sean de interés para la clase
    def info(self):
        print("El nombre del municipio es ", self.nom, "y su clave inegi es", self.cve, " y tiene una superficie de ", self.sup)
    
    def supKm(self, valor):
        if valor > 10000:
            print("Es un municipio grande")
        else:
            print("Es un municipio pequeño")
    
Mun = Municipio("Toluca", "106", 7435435, 4700, 453634)
print(Mun.getNom())
Mun.setNom("Metepec")
Mun.setCve("103")
print(Mun.getNom())
print(Mun.info())

class colonia(Municipio):
    ah = 0

    # Definición de constructor
    def __init__ (self, areaH, nombre, clave, pobTotal, altitud, superficie):
        super().__init__(nombre, clave, pobTotal, altitud, superficie)
        self.ah = areaH
    # Metodos de la clase GET y SET
        def getAH(self):
            return self.ah
        def setAH(self, ah):
            self.ah = ah
    # Metodos alternativos
    def infoAH(self, value):
        self.AH = self.ah + value
        self.info()
        print(self.nom, "cuenta con ", self.ah, "áreas homogéneas") #self.nom es una atrabuto de la clase Municipio.
        
col = colonia(5,"Toluca","106",7435435,4700,453634)
print(col.infoAH(3))
print(col.getNom()) # La clase colonia no tiene el método getNom() pero es accesible mediante la herencia que 