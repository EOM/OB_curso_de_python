def abrir_y_escribir_dos_veces():
    # Crear el archivo de texto y escribe
    f = open('mi_archivo.txt', 'w')
    f.write('Ejercicio 8.1 crear y escribir\n')
    f.close()

    # Abrir el archivo y escribir de nuevo
    f = open('mi_archivo.txt', 'a')
    f.write('Abrir de nuevo y escribir de nuevo.\n')
    f.close()


# Ejercicio 8.1
print('Se va a genear el archivo: "mi_archivo.txt"')
abrir_y_escribir_dos_veces()
print('Fin del proceso ya se creo el archivos.')