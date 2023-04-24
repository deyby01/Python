class Vehiculo:

    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas

class Coche(Vehiculo):

    def __init__(self, color, ruedas, puertas, velocidad, cilindrada):
        super().__init__(color, ruedas, puertas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

c = Coche("rojo", 4, 2, 320, 2000)
print(f"Color: {c.color}")
print(f"Ruedas: {c.ruedas}")
print(f"Puertas: {c.puertas}")
print(f"Velocidad: {c.velocidad}")
print(f"Cilindrada: {c.cilindrada}")