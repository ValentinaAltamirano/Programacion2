# Vamos a crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI.
# Construye los siguientes métodos para la clase:
# Un constructor, donde los datos pueden estar vacíos.
# Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.
# mostrar(): Muestra los datos de la persona.
# esMayorDeEdad(): Devuelve un valor lógico indicando si es mayor de edad.

class Persona:
    def __init__(self, nombre, dni, edad):
        self.nombre = nombre
        self.dni = dni
        self.edad = edad

    def validarNombre(self, nombre):
        if nombre.isnumeric():
            nom = input("El nombre es invalido, ingrese el nombre nuevamente: ")
            self.validarNombre(nom)
        elif len(nombre) <= 2 and len(nombre) != 0:
            nom = input("El nombre es invalido, ingrese el nombre nuevamente: ")
            self.validarNombre(nom)
        else:
            self.setNombre(nombre)

    def validarEdad(self, edad):
        if edad.isnumeric():
            if int(edad) >= 0 and int(edad) < 100:
                self.setEdad(int(edad))
            else:
                edadN = input("La edad es invalida, ingrese la edad nuevamente: ")
                self.validarEdad(edadN)
        elif edad == "":
            pass
        else:
            edadN = input("La edad es invalida, ingrese la edad nuevamente: ")
            self.validarEdad(edadN)

    def validarDni(self, dni):
        if dni.isnumeric():
            if len(dni) >= 6 and len(dni) <= 8:
                self.setDni(int(dni))
            else: 
                dniN = input("El dni es invalido, ingrese el dni nuevamente: ")
                self.validarDni(dniN)
        elif dni == "":
            pass
        else:
            dniN = input("El dni es invalido, ingrese el dni nuevamente: ")
            self.validarDni(dniN)
    
    def getNombre(self):
        return self.nombre

    def getDni(self):
        return self.dni

    def getEdad(self):
        return self.edad

    def setNombre(self,nombre):
        self.nombre= nombre
    
    def setDni(self,dni):
        self.dni= dni

    def setEdad(self,edad):
        self.edad= edad

    def mostrar(self):
        print(f'Nombre: {self.getNombre()}, dni: {self.getDni()} edad: {self.getEdad()}')

    def mayorEdad(self):
        if self.edad == "":
            pass
        elif self.edad >= 18:
            print("Es mayor de edad")
        else:
            print("Es menor de edad")

nom = input("Ingrese nombre: ")
dni = input("Ingrese dni: ")
edad = input("Ingrese edad: ")
p1 = Persona(nom, dni, edad)
p1.validarEdad(edad)
p1.validarDni(dni)
p1.validarNombre(nom)
p1.mostrar()
p1.mayorEdad()
