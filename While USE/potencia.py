base=int(input("digite la base: "))
exponente=int(input("digite el exponente: "))
numero=0
while numero<=exponente:
    print(f"{base}^{numero}={base**numero}")
    numero=numero+1