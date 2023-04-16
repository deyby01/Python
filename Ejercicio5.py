'''
Escribe una función que pueda decirte si un año (número entero) es bisiesto o no.
'''

def es_bisiesto(anio):
    # Calculo para saber si es o no
    if anio % 4 == 0 and anio % 100 != 0:
        return True
    else:
        return False
    
anioo = int(input("Ingrese un año para saber si es Bisiesto: "))

print(es_bisiesto(anioo))