roten_ur = []
x=-10
while True:
    if x==11:
        break
    roten_ur.append(x**2)
    x += 1
print(roten_ur)


plt.plot(roten_ur)
plt.show()



chessboard = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
lista = ["1", "2", "3", "4", "5", "6", "7", "8"]

x = list("ABCDEFGH")
x2 = list-("12345678")
x3 = 0
for i in range(8):
    print("")
    for i in range(8):
        x5= list(x[i]+x2[x3])
        print(x5, end= " ")
    x3 += 1

chessboard = ["abcdefgh"]
for chess in chessboard:
    print(chessboard)






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



