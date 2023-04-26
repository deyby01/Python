import tkinter as tk

class App:
    def __init__(self, master):
        self.master = master
        self.radio_var = tk.IntVar(value=-1)
        
        # Crear los tres RadioButton
        self.radio1 = tk.Radiobutton(master, text="Opción 1", variable=self.radio_var, value=1)
        self.radio2 = tk.Radiobutton(master, text="Opción 2", variable=self.radio_var, value=2)
        self.radio3 = tk.Radiobutton(master, text="Opción 3", variable=self.radio_var, value=3)
        
        # Crear los botones "Mostrar" y "Reiniciar"
        self.show_button = tk.Button(master, text="Mostrar", command=self.show_selection)
        self.reset_button = tk.Button(master, text="Reiniciar", command=self.reset_selection)
        
        # Posicionar los widgets
        self.radio1.grid(row=0, column=0)
        self.radio2.grid(row=1, column=0)
        self.radio3.grid(row=2, column=0)
        self.show_button.grid(row=3, column=0)
        self.reset_button.grid(row=3, column=1)
    
    def show_selection(self):
        selected_value = self.radio_var.get()
        if selected_value == 1:
            print("Ha seleccionado la opción 1")
        elif selected_value == 2:
            print("Ha seleccionado la opción 2")
        elif selected_value == 3:
            print("Ha seleccionado la opción 3")
        else:
            print("No ha seleccionado ninguna opción")
    
    def reset_selection(self):
        self.radio_var.set(-1)

# Crear la ventana principal
root = tk.Tk()
root.title("Lista de RadioButton")

# Crear la aplicación
app = App(root)

# Ejecutar el bucle de eventos
root.mainloop()
