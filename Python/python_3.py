# 3. Escribí un programa que solicite al usuario dos números y los almacene en dos variables. 
# En otra variable, almacena el resultado de la suma de esos dos números y luego muestra ese resultado en pantalla. 
# A continuación, el programa debe solicitar al usuario que ingrese un tercer número, el cual se debe almacenar en una nueva variable. 
# Por último, muestra en pantalla el resultado de la multiplicación de este nuevo número por el resultado de la suma anterior.


#1
print("Bienvenido, ejercicio 3")
value_number1 = float(input("Ingrese un numero: "))
value_number2 = float(input("Ingrese un segundo numero: "))
total_value = value_number1+value_number2
print("El resultado de su suma es: ", total_value)

#2
value_number3 = float(input("Ingrese un tercer numero: "))
operation = value_number3*total_value
print("El resultado de su operacion es: ",operation)
