from time import sleep    # para el tiempo
from os import system    #para limpiar el texto
calle=0
while calle<=20:
    sleep(1)
    system("cls")
    if calle==15:
        print("llegaste a la calle 15 ")
    print(calle)
    calle=calle+1