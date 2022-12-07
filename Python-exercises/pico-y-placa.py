#SIN TERMINAR

'''
Reto 2 - PICO Y PLACA


Para mantener la movilidad en las ciudades
 se ha venido utilizaNdo los llamados
  “Pico y Placa”, que consiste en prohibir 
  la circulación de vehículos según la placa
   del mismo. En una ciudad se quiere limitar
    la circulación de carros (c) y motos (m) 
    y se decide hacer un Pico y Placa según 
    el último caracter de la placa, los carros
     tienen un dígito al final (0-9) y las
      motos tienen una letra al final (A-Z).
       El esquema del pico y placa es el 
       siguiente:

```python
"Nota 1:"

Lunes (l), Martes (m) y Miercoles (x): se prohíbe 
la circulación de carros terminados en dígito
 par o cero, y las motos que terminen en las
  letras A a la M.


"Nota 2:

Jueves (j), Viernes (v) y Sábado (s): se prohíbe
 la circulación de los carros terminados en 
 dígito impar y las motos que terminen en las
  letras N a la Z.



"Nota 3:

Domingo (d) todos pueden salir.

```


## Requerimientos:

Escribe un programa(Función) que reciba los 
siguientes parámetros en el mismo orden:


+ El tipo de vehículo como una letra en {c,m}

+ El día de la semana como una letra en {l,m,x,j,v,s,d}

+ Placa del vehículo en {0-9} u {A-Z}

El programa debe inidicar si el vehículo puede o no salir ese día.

'''
'''
if len(input_str) > 15:
    print "Error! Only 15 characters allowed!"
    sys.exit()
    
    
'''    
veh_type=input("Ingrese el tipo de su vehiculo m(moto) y c (carro): ")
veh_type=veh_type.upper()
placa=input("Ingrese la placa de su vehiculo: ")



#limite_placa = placa[:6]

#Inputs
dia=input("Ingrese su dia de pico y placa: l(lunes) m(martes) x(miercoles) j(jueves) v(viernes) s(sabado) d(domingo): ")
dia=dia.upper() #Uppercase Input

letrasAM=["A","B","C","D","E","F","G","H","I","J","K","L","M"]


#Funtion
def PyP(veh_type, placa, dia):

#Limit characters in the string input
  if len(placa) =6
    return "Valor correcto"
  else
    return "Error""

#Condicion de días  
      if dia=="L" or dia=="M" or dia=="X":
        if veh_type=="C":
            ultimo_digito_placa=placa[-1]
            ultimo_digito_placa=int(ultimo_digito_placa)
            if ultimo_digito_placa %2==0:
                print ("Su vehículo con la matricula", placa, "Tiene pico y placa")
            else:
                print ("El vehiculo con la matricula", placa, "no tiene pico y placa")
            
        elif veh_type=="M":
            ultimo_digito_placa=placa[-1]
            ultimo_digito_placa=ultimo_digito_placa.upper()
            x=letrasAM.count(ultimo_digito_placa)
            if x>0:
                return "tiene pico y placa"
            else:
                return "No tiene pico y placa"
