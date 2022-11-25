class Alumno:

    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def __str__(self):
        if self.nota >= 5:
            return f'Alumno: {self.nombre}, con nota {self.nota}, APROBÓ'
        else:
            return f'Alumno: {self.nombre}, con nota {self.nota}, NO APROBÓ'


alumno1 = Alumno("Pepe", 8)
print(alumno1)