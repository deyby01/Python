'''En este segundo ejercicio, tendréis que crear un archivo py y dentro crearéis una clase 
Vehículo, haréis un objeto de ella, lo guardaréis en un archivo y luego lo cargamos.'''

# Importamos la libreria pickle

import pickle

class Vehiculo:

    marca = ""
    precio = 0

    def __init__(self, marca, precio):
        self.marca = marca
        self.precio = precio

    def getMarca(self):
        return self.marca
    


#   Creo el objeto de donde voy a llamar a la clase
#v1 = Vehiculo("Mercedez", 20000000)
#   Verifico
#print(v1.getMarca())


#   Ahora vamos a cargar los datos
#f = open("vehiculo.bin", "wb")
#pickle.dump(v1, f)
#f.close()


#   Ahora vamos a traer los datos cargados.
f = open("vehiculo.bin", "rb")
vehiculo = pickle.load(f)
f.close()


#   Vamos a probar que los datos esten
print(vehiculo.getMarca(), "Precio: ", vehiculo.precio)