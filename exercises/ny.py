# _________________________nummer gissar lek fast ai gissar_________________________




x = 50
gissningar = 0
i = int(input("skriv ditt nummer: "))
while True:
    if x > i:
        x = x-1
        gissningar += 1
        print(x)
    elif x < i:
        gissningar += 1
        x = x+1
        print(x)
    else:
        print(f"CORREKT AI det tog dig bara:{gissningar} gissningar")
        break


# lite bättre

x = 50
gissningar = 0
i = int(input("skriv ditt nummer: "))
while True:
    if x > i:
        gissningar += 1
        x = x-2
        print(x)
    elif x < i:
        gissningar += 1
        x = x+5
        print(x)
    else:
        print(f"CORREKT AI det tog dig bara:{gissningar} gissningar")
        break



