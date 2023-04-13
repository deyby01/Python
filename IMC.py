peso = float(input("Ingresa tu peso en Kg.: "))
estatura = float(input("Ingresa tu estatura en Metros: "))

calculo = peso/(estatura**2)
calculo = round(calculo, 2)

if calculo < 18.5:
    print(f"Tu indice de masa corporal es: {calculo}, Bajo peso.")
elif calculo > 18.5 and calculo < 24.9:
    print(f"Tu indice de masa corporal es: {calculo}, Adecuado.")
elif calculo > 25.0 and calculo < 29.9:
    print(f"Tu indice de masa corporal es: {calculo}, Sobrepeso.")
elif calculo > 30.0 and calculo < 34.9:
    print(f"Tu indice de masa corporal es: {calculo}, Obesidad grado 1.")
elif calculo > 35.0 and calculo < 39.9:
    print(f"Tu indice de masa corporal es: {calculo}, Obesidad grado 2.")
else:
    print(f"Tu indice de masa corporal es: {calculo}, Obesidad grado 3.")