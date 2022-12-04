# Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado.

weigth = float(input("Ingrese su peso (Kilogramos): "))
height = float(input("Ingrese su estatura (Metros): "))
imc = weigth/(height)**2

print("El IMC obtenido es igual a:", imc,"kg/m²" )