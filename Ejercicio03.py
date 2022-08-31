# Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva
#clase CuantaJoven que deriva de la anterior. Cuando se crea esta nueva clase, además del
#titular y la cantidad se debe guardar una bonificación que estará expresada en tanto por
#ciento.Construye los siguientes métodos para la clase:
# Un constructor.
# Los setters y getters para el nuevo atributo.
# En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad.,
#por lo tanto hay que crear un método esTitularValido() que devuelve verdadero
#si el titular es mayor de edad pero menor de 25 años y falso en caso contrario.
# Además la retirada de dinero sólo se podrá hacer si el titular es válido.
#El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la
#bonificación de la cuenta.
#Piensa los métodos heredados de la clase madre que hay que reescribir.

from Ejercicio02 import Cuenta 

class CuentaJoven(Cuenta):
    def __init__(self,titular, cantidad, bonificacion, edad):
        super().__init__(titular, cantidad) #llamo 
        self.setEdad(edad)
        self.setBonificacion(bonificacion)
    
    def setEdad(self, edad):
        if edad.isnumeric():
            if int(edad) > 0 and int(edad) < 100:
                self.edad = int(edad)
            else:
                edadN = input("La edad es invalida, ingrese la edad nuevamente: ")
                self.setEdad(edadN)
        else:
            edadN = input("La edad es invalida, ingrese la edad nuevamente: ")
            self.setEdad(edadN)
    
    def getEdad(self):
        return self.edad

    def setBonificacion(self, bonificacion):
        if bonificacion.isnumeric():
            if self.esTitularValido():
                self.bonificacion = self.cant * int(bonificacion) / 100
                self.cant += self.bonificacion
            else:
                self.bonificacion = 0
        else:
            edadN = input("La edad es invalida, ingrese la edad nuevamente: ")
            self.validarEdad(edadN)
        

    def getBonificacion(self):
        return self.bonificacion

    def esTitularValido(self):
        if self.getEdad() >= 18 and self.getEdad() < 25:
            return True
        else:
            print("La edad no cumple con la cuenta Joven")
            return False
    
    def retirar(self):
        if self.esTitularValido():
            cant = input("Ingrese cantidad a retirar en cuenta Joven: ")
            super().retirar(cant)
        else:
            print("No puede retirar dinero ya que no cumple con la edad")
    
    def mostrar(self):
        super().mostrar()
        print(f"La cuenta tiene una bonificacion del ${self.getBonificacion()}")

n = input("Nombre cuenta Joven: ")
c = input("Monto de la cuenta Joven: ")
b = input("Bonificacion de cuenta Joven: ")
e = input("Ingrese la edad: ")
j1 = CuentaJoven(n, c, b, e)
j1.retirar()
j1.mostrar()