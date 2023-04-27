import sqlite3

# Conectamos con la base de datos
conn = sqlite3.connect('alumnos.db')

# Creamos la tabla Alumnos
conn.execute('''CREATE TABLE Alumnos
                (id INTEGER PRIMARY KEY,
                 nombre TEXT,
                 apellido TEXT);''')

# Insertamos datos en la tabla
conn.execute("INSERT INTO Alumnos (id, nombre, apellido) VALUES (1, 'Juan', 'Pérez')")
conn.execute("INSERT INTO Alumnos (id, nombre, apellido) VALUES (2, 'María', 'García')")
conn.execute("INSERT INTO Alumnos (id, nombre, apellido) VALUES (3, 'Pedro', 'Gómez')")
conn.execute("INSERT INTO Alumnos (id, nombre, apellido) VALUES (4, 'Laura', 'Rodríguez')")
conn.execute("INSERT INTO Alumnos (id, nombre, apellido) VALUES (5, 'José', 'Martínez')")
conn.execute("INSERT INTO Alumnos (id, nombre, apellido) VALUES (6, 'Ana', 'Sánchez')")
conn.execute("INSERT INTO Alumnos (id, nombre, apellido) VALUES (7, 'Luis', 'Hernández')")
conn.execute("INSERT INTO Alumnos (id, nombre, apellido) VALUES (8, 'Lucía', 'López')")

# Guardamos los cambios en la base de datos
conn.commit()

# Buscamos un alumno por nombre y mostramos los datos
cursor = conn.execute("SELECT id, nombre, apellido FROM Alumnos WHERE nombre=?", ('Juan',))
for row in cursor:
    print("ID = ", row[0])
    print("Nombre = ", row[1])
    print("Apellido = ", row[2])

# Cerramos la conexión con la base de datos
conn.close()
