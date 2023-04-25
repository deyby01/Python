'''
En este ejercicio, tendréis que crear un archivo py donde creéis un archivo txt, 
lo abráis y escribáis dentro del archivo. Para ello, tendréis que acceder dos veces al archivo creado.
'''

# Creamos y abrimos el archivo
f = open("primerFichero.txt", "w")
f.write("Primera linea\n")
f.write("segunda linea\n")
f.write("tercera linea\n")
f.write("cuarta linea\n")
f.close()

# Aqui lo abrimos por segunda vez para leer el contenido.
f = open("primerFichero.txt", "r")
datos = f.read()
f.close()

print(datos)