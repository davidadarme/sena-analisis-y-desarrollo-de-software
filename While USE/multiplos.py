ini=int(input(" digite el inicio: "))
fin=int(input("digite el final : "))
multiplo=int(input("digite el multiplo : "))
while ini<=fin:
    if ini%multiplo==0:
        print(ini)
    ini=ini+1