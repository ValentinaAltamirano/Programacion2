#Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una
#persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es
#opcional. Construye los siguientes métodos para la clase:
# Un constructor, donde los datos pueden estar vacíos.
# Los setters y getters para cada uno de los atributos. El atributo no se puede
#modificar directamente, sólo ingresando o retirando dinero.
# mostrar(): Muestra los datos de la cuenta.
# ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad
#introducida es negativa, no se hará nada.
# retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en
#números rojos.

class Cuenta():
    def __init__(self, titular, cant):
        self.setTitular(titular)
        self.setCantidad(cant)
    
    def getTitular(self):
        return self.titular
    
    def getCantidad(self):
        return self.cant

    def setTitular(self,titular):
        if titular != "":
            self.titular = titular
        else:
            nuevoTitular = input("Ingreso el nombre incorrecto. ingrese nuevamente: ")
            self.setTitular(nuevoTitular)
    
    def setCantidad(self,cant):
        self.cant = self.validarCantidad(cant)

    def validarCantidad(self,cant):
        if cant != "":
            if cant.isnumeric():
                return int(cant)
            else:
                nuevaCantidad = input("Ingreso una cantidad incorrecta, ingrese nuevamente: ")
                self.validarCantidad(nuevaCantidad)            
        else:
            return 0

    def ingresar(self, cantidad):
        cantidad = self.validarCantidad(cantidad)
        if cantidad > 0:
            self.cant += cantidad
        else: 
            nuevaCant = input("Ingreso una cantidad incorrecta, ingrese nuevamente: ")
            self.ingresar(nuevaCant)
    
    def retirar(self, cantidad):
        cantidad = self.validarCantidad(cantidad)
        if cantidad > 0:
            self.cant -= cantidad
        else: 
            nuevaCant = input("Ingreso una cantidad incorrecta, ingrese nuevamente: ")
            self.retirar(nuevaCant)

    def mostrar(self):
        print(f'Titular: {self.getTitular()} Cantidad: {self.getCantidad()}')
    

titular = input("Ingrese el nombre del titular: ")
cantidad = input("Ingrese la cantidad: ")
cuenta1 = Cuenta(titular, cantidad)
cuenta1.mostrar()
cantidadIngresar = input("Ingrese la cantidad a ingresar: ")
cuenta1.ingresar(cantidadIngresar)
cuenta1.mostrar()
cantidadRetirar = input("Ingrese la cantidad a retirar: ")
cuenta1.retirar(cantidadRetirar)
cuenta1.mostrar()
