Aqui dejo un pequeño resumen de como hice mi programa para hacerlo
un poco mas entendible en caso de no entender como lo hice.

Lo primero que hice fue crear las funciones, las cuales tienen una 
funcion en especifico:

1.- La funcion openFile() se encarga de abrir el archivo de texto.
2.- La funcion isEmpty() se encarga de verificar si el archivo esta
vacio o no, para ello utilize un operador ternario de if/else que lee
apartir de la segunda fila, ya que la primera no se cuenta.
3.- La funcion newContact() se encarga de crear un nuevo contacto,
lo guarda en una lista y despues muestra un mensaje de que los datos
se guardaron con exito.
4.- la funcion showAgenda() se encarga de mostrar los datos que hay
en el archivo de texto para su visualización.
5.- Quise crear una funcion con el menu para tener un codigo mas 
limpio.

Despues cree el menu utilizando el bucle while y lo active usando 
un booleano con valor True, hasta que rompa el bucle con un break
y en caso de que el usuario ingrese una opcion que no este en el
menu vuelve a preguntar por la opcion.

en la opcion 3 ingrese un pequeño texto, para que el usuario sepa
que es lo que esta visualizando.

y hasta aqui queda la explicacion de como hice este codigo.

pd: Lo hize en ingles por que creo que se ve mejor y mas elegante jsjsjjjsjsjs