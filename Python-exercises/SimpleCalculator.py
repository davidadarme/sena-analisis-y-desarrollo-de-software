#Choose the operation option 1, 2, 3, 4 
print("OPERACION ARITMETICA CON DOS DATOS")

#Add function
def add (x, y):
    return x+y

#Substract function
def sub (x, y):
    return x-y

#Multiplication function
def mult (x, y):
    return x*y

#Division function
def div (x, y):
    return x/y
 
 #Select operation
NumValueInput = input("\n1. Suma \n2. Resta \n3. Multiplicacion \n4. Divisio \n Seleccione la operacion que desea realizar: ")

#Input data a, b
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

#Operation result
if NumValueInput == '1':
    print("El resultado de la operacion", num1,"+",num2,"=", add(num1, num2))

elif NumValueInput == '2':
    print("El resultado de la operacion", num1,"-",num2,"=", sub(num1, num2))

elif NumValueInput == '3':
    print("El resultado de la operacion", num1, "*" ,num2, "=", mult(num1, num2))

elif NumValueInput == '4':
    print("El resultado de la operacion", num1, "/" ,num2, "=", div(num1, num2))
