numero=int(input("digite un numero min: "))
max=int(input("digite un numero max: "))
while numero<=max:
    contador=0
    for i in range(1,numero+1):
        if(numero%i==0):
          contador=contador+1
    if (contador==2):
        print(numero)
    numero=numero+1    