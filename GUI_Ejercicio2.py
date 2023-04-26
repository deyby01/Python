import tkinter as tk

# Crear ventana
ventana = tk.Tk()
ventana.title("Interfaz sencilla")

# Crear lista de elementos seleccionables
opciones = ["Opción 1", "Opción 2", "Opción 3"]
variable_seleccion = tk.StringVar(value=opciones[0])  # Valor inicial
lista_opciones = tk.OptionMenu(ventana, variable_seleccion, *opciones)
lista_opciones.pack()

# Crear label
label_texto = tk.Label(ventana, text="Texto del label")
label_texto.pack()

# Mostrar ventana
ventana.mainloop()
