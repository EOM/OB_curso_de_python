import calculadora as cal

valor1 = 10
valor2 = 2

print('-------------INICIO--------------')
print("Sumar (", valor1, " + ", valor2, ") es: ", cal.suma(valor1, valor2))
print("Resta (", valor1, " - ", valor2, ") es: ", cal.resta(valor1, valor2))
print("Multiplicar (", valor1, " * ", valor2, ") es: ", cal.multiplicar(valor1, valor2))
print("Dividir (", valor1, " / ", valor2, ") es: ", cal.dividir(valor1, valor2))
valor1 = 0
print("Dividir por cero (", valor1, " / ", valor2, ") es: ", cal.dividir(valor1, valor2))
print('--------------FIN----------------')
