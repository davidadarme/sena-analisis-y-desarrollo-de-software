# Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. 
# Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. 

'''
Calcular y mostrar por pantalla la cantidad de ahorros tras el primer
'''

print("Welcome to Nubank")

#User
username = input("Ingrese su nombre: ")
print("Welcome back", username)

#CashData
cash_data = int(input("Ingrese la cantidad de dinero depositada: "))
interest_rate = 0.04
total_cash= cash_data * (1 + interest_rate)

#Proccess
cash_data_year1 = cash_data * (1 + interest_rate)
print("La cantidad de ahorros durante el primer año:", cash_data_year1)

cash_data_year2 = cash_data * (1 + interest_rate*2)
print("La cantidad de ahorros durante el primer año:", cash_data_year2)

cash_data_year3 = cash_data * (1+ interest_rate*3)
print("La cantidad de ahorros durante el primer año:", cash_data_year3)
