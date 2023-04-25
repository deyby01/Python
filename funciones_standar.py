# Pedir al usuario una lista de países
paises = input("Ingresa una lista de países separados por comas: ")

# Separar los países y crear una lista
lista_paises = paises.split(",")

# Eliminar países repetidos utilizando un set
conjunto_paises = set(lista_paises)

# Ordenar alfabéticamente la lista de países
lista_ordenada = sorted(conjunto_paises)

# Mostrar la lista de países ordenados por consola
print("Los países ordenados alfabéticamente son: ", ", ".join(lista_ordenada))
