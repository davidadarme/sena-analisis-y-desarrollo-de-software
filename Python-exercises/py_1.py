    #Ejercicio 1
       
MData_value = float(input("Ingrese la cantidad de hombres: "))
FData_value = float(input("Ingrese la cantidad de mujeres: "))  # %/100*total
total_data_value = MData_value+FData_value
MPercent = (MData_value *100)/ total_data_value
FPercent = (FData_value *100)/ total_data_value

print("El porcentaje de hombres es", MPercent, " y el porcentaje de mujeres es", MPercent)
