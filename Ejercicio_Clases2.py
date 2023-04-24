class Alumno:

    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir_datos(self):
        print(f"El nombre del alumno es: {self.nombre}")
        print(f"La nota del alumno es: {self.nota}")

    def verificar_nota(self):
        if self.nota >= 5:
            print(f"El alumno {self.nombre} ha aprobado.")
        else:
            print(f"El alumno {self.nombre} ha reprobado.")
        
alumno = Alumno("David", 6)
alumno.imprimir_datos()
alumno.verificar_nota()