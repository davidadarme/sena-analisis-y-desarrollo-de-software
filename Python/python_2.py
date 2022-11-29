#  A continuación, el programa debe solicitar al usuario que ingrese un número entero y guardarlo en otra variable. 
# En una tercera variable se deberá guardar el resultado de la suma de los dos números ingresados por el usuario. 
# Por último, se debe mostrar en pantalla el texto "EIT resultado de la suma es [suma]". donde [suma]" se reemplazará por el resultado de la operación

print("Bienvendo, Suma de un numero decimal y un numero entero ")

DecimalsNumbers = float(input("Ingrese un numero con decimales: "))
IntegersNumbers = float(input("Ingrese un numero entero: "))
total_value = DecimalsNumbers+IntegersNumbers

print("El resultado de la suma es:", total_value)
