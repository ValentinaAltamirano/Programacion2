# Vamos a crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI.
# Construye los siguientes métodos para la clase:
# Un constructor, donde los datos pueden estar vacíos.
# Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.
# mostrar(): Muestra los datos de la persona.
# esMayorDeEdad(): Devuelve un valor lógico indicando si es mayor de edad.

class Persona():
    def __init__(self, nombre, edad, dni):
        self.nombre = nombre;
        self.edad = edad;
        self.dni = dni;

    @property
    def getNombre(self):
        return self.nombre

    @property
    def getEdad(self):
        return self.edad

    @property
    def getDni(self):  
        return self.dni
    
    def setNombre(self, nom):
        self.nom = nom
    
    def setEdad(self, edad):
        self.edad = edad
    
    def setDni(self, dni):
        self.dni = dni

    def validarEdad(self):
        return type(self.getEdad()) == int
    
    def esMayorDeEdad(self):
        if self.validarEdad() == True:
            if self.getEdad() >= 18:
                print("True")
            else:
                print("False")
        else:
            print("La edad ingresada es invalida")

    def __str__(self):
        print(f'Nombre: {self.getNombre()} Edad: {self.getEdad()} Dni: {self.getDni()}')


per1 = Persona('Jorge', 18, 123131)
per1.__str__()
per1.esMayorDeEdad()

per2 = Persona('Sebatian', '18', 4324131)
per2.__str__()
per2.esMayorDeEdad()