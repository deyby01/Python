def openFile():
    route = "Control_N4\contactos.txt"
    file = open(route , "r")
    return file


def isEmpty():
    file = openFile()
    content = file.readlines()
    file.close()
    return len(content) > 1


def newContact():
    print("=== New Contact ===")
    route = "Control_N4\contactos.txt"
    f = open(route, "a")
    n = input("Enter name: ")
    p = int(input("Enter phone: "))
    data = [n, p]
    f.write(f"\n{data[0]};{data[1]}")
    print("New contact created.")


def showAgenda():
    show = openFile()
    content = show.read()
    print(content)
    show.close()


def menu():
    print("   === Menu ===  ")
    print("\n 1.- Abrir archivo\n 2.- Estado de la agenda\n 3.- Mostrar datos agenda\n 4.- Crear contacto\n 5.- Salir\n")

while True:
    
    menu()
    option = int(input("Enter option: "))
    if option == 1:
        data = openFile()
        print("file opened successfully\n")
        
    elif option == 2:
        print("if the agenda is empty it will say (False), but if it contains data it will say (True)")
        print()
        print(isEmpty())
        print()
    
    elif option == 3:
        showAgenda()
        print()
    
    elif option == 4:
        newContact()
        print()
    
    elif option == 5:
        print("FINISHED PROGRAM.")
        print()
        break

    else:
        print("invalid option, enter a correct one.")
        print()