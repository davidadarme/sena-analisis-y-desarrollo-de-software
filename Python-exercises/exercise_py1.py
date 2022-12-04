#Escribir un programa que lea un entero positivo, n, introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta n. La suma de los n primeros enteros positivos puede ser calculada de la siguiente forma:  suma=n(n+1)2

print("Escribir un programa que lea un entero positivo, n, introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta n. La suma de los n primeros enteros positivos puede ser calculada de la siguiente forma: suma=n(n+1)2")

n = int(input("Ingrese un numero ENTERO POSITIVO: ")) #Input
AddOperator = n*(n+1) / 2 #Operator

if n<= 0: #Condiciones
    print("Error 404, no cumple la condicion requerida de ingresar un numero ENTERO POSITIVO")
else: 
    print ("La suma de", n, "es igual a", AddOperator)