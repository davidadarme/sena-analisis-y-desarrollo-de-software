#Escribir un programa que pregunte el nombre del usuario y un número entero e imprima el 
# nombre del usuario tantas veces como el número introducido.

print("Escribir un programa que pregunte el nombre del usuario y un número entero e imprima el nombre del usuario tantas veces como el número introducido.")

Username = str(input("Ingrese su nombre: ")) #Username
Int_number = int(input("Ingrese un numero entero: ")) #Int_number

for x in range (Int_number) :
    print(Username)

    if Int_number <= 0: #Condiciones
        print("Error 404, no cumple la condicion requerida de ingresar un numero ENTERO POSITIVO")