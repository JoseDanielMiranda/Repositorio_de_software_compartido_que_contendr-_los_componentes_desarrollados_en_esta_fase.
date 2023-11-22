class Estudiante:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, nueva_edad):
        self._edad = nueva_edad

    def estudiar(self, materia):
        return f"{self._nombre} está estudiando {materia}."

    def presentarse(self):
        return f"Hola, soy {self._nombre} y tengo {self._edad} años."

# Uso de la clase
estudiante1 = Estudiante("Juan", 20)

# Acceder a atributos y propiedades
print(estudiante1.nombre)  # Salida: Juan
print(estudiante1.edad)    # Salida: 20

# Llamar a métodos
print(estudiante1.estudiar("Matemáticas"))  # Salida: Juan está estudiando Matemáticas.
print(estudiante1.presentarse())            # Salida: Hola, soy Juan y tengo 20 años.

# Modificar atributos mediante propiedades
estudiante1.nombre = "Ana"
estudiante1.edad = 22

# Verificar cambios
print(estudiante1.presentarse())  # Salida: Hola, soy Ana y tengo 22 años.
