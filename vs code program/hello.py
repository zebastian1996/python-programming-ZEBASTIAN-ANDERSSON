# import random
# import matplotlib.pyplot as plt

# tärningskasten = []
# for tärning in range(10):
#     kast = random.randint(1,6)
#     tärningskasten.append(kast)
#     tärningskasten.sort()
# print(tärningskasten)
# print(tärningskasten[::-1])


#______________________roten ur lek____________________

# roten_ur = []
# x=-10
# while True:
#     if x==11:
#         break
#     roten_ur.append(x**2)
#     x += 1
# print(roten_ur)


# plt.plot(roten_ur)
# plt.show()



# chessboard = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
# lista = ["1", "2", "3", "4", "5", "6", "7", "8"]

# x = list("ABCDEFGH")
# x2 = list-("12345678")
# x3 = 0
# for i in range(8):
#     print("")
#     for i in range(8):
#         x5= list(x[i]+x2[x3])
#         print(x5, end= " ")
#     x3 += 1

# chessboard = ["abcdefgh"]
# for chess in chessboard:
#     print(chessboard)






#_________________________nummer gissar lek fast ai gissar_________________________




# x = 50
# gissningar = 0
# i = int(input("skriv ditt nummer: "))
# while True:
#     if x > i:
#         x = x-1
#         gissningar += 1
#         print(x)
#     elif x < i:
#         gissningar += 1
#         x = x+1
#         print(x)
#     else:
#         print(f"CORREKT AI det tog dig bara:{gissningar} gissningar")
#         break


# # lite bättre

# x = 50
# gissningar = 0
# i = int(input("skriv ditt nummer: "))
# while True:
#     if x > i:
#         gissningar += 1
#         x = x-2
#         print(x)
#     elif x < i:
#         gissningar += 1
#         x = x+5
#         print(x)
#     else:
#         print(f"CORREKT AI det tog dig bara:{gissningar} gissningar")
#         break















#______________________________________-multiplikations leken-________________________________
# import random

# while True:
#     x = random.randint(1,10)
#     y = random.randint(1,10)

#     resultat = x * y
#     gissning = int(input(f"vad blir {x} gånger {y}?\n:"))


#     print(gissning)
#     if gissning == resultat:
#         print(f"du hade rätt det va {resultat} ")
#     else:
#         print(f'fel det skulle vara"{resultat}" och du gissade på {gissning}')




#________________________________________-dice rolls-_______________________________

#import random

# summa = 0
# for i in range(10):
#     dice = random.randint(1, 6)
#     if dice == 6:
#         summa += 1
# print(summa)


#while True:








#________________________________________test på tärningskast__________________________________________________

# import random

# kast = []
# nummer = []
# sexor = []


# def kasta(a,b):
#     for i in range(10):
#         kast = random.randint(1,6)
#         nummer.append(kast)
#         sexa = [sexor.append(kast) if kast == 6 else "du fick inga"]
#         print(kast)
#     print(f"du fick {len(sexor)}:st ")
#     nummer.sort()
#     print(nummer)
# kasta(1,10)







#_______________________________-counting words__________________________




# ordet = ("A picture says more than a thousand words, a matematical formula says more than a thousand pictures")
# längden = ordet.split()
# print(längden)
# print(len(längden))


#_________________________________-count vowels-_________________


# vowels = ("aeiouyåäö")
# input = ("Pure mathematics is, in its way, the poetry of logical ideas")
# antal = 0
# for vokaler in vowels:
#     antal += input.count(vokaler)

# print(antal)


#_______________________________________incrypta meddelanden för spoin firman______________________________________________


# --------kan göra lite mer saker som att få decrypta ordet som allternativ direkt---------


# def incrypt():
#     ordet = input("skriv allt du vill incrypta: ")
#     x = [ord(i) + 1 for i in ordet]
#     x = [chr(i) for i in x]
#     print(f"här är den incryptade versionen: {"".join(x)}")


# def unincrypt():
#     print("decryptat")
#     ordet = input("vad vill du decrypta?: ")
#     x = [ord(i) - 1 for i in ordet]
#     x = [chr(i) for i in x]
#     print(f"här är ditt ord du kan skicka vidare\n{"".join(x)}")


# print('tjena och välkommen till spoin firman. du kommer få 2 alternativ nu\nskriv "1" för att incrypta ett meddelande\nskriv "2"' \
# ' för att uncrypta ett meddlande\nvill du avsluta så skriver du "3" eller "avsluta"')

# spion = True
# while spion:
    
#     handling = input('så vad vill du göra?: ')
    

#     if handling == "1":
#         incrypt()
        

#     elif handling == "2":
#         unincrypt()


#     elif handling == "3" or handling.lower == "avsluta":
#         print("vi tackar för oss och lycka till på uppdraget")
#         spion = False

#     else:
#         hjälp = input('det va inget alternativ vill du ha alternativen igen? "ja": ')
        
#         if hjälp == "ja":
#             print('hejsan vi ska hjälpa dig. alternativen du har att välja på är\n"1" för att incrypta ett meddelande\n' \
#             'sen har du också "2" för att decrypta det')

#         elif hjälp != "ja":
#             print()


#_____________________________________scatter print_____________________________

# import numpy as np
# import matplotlib.pyplot as plt

# x_in = []
# y_in = []

# x_ut = []
# y_ut = []


# for i in range(40000):
#     x = np.random.uniform(-1, 1)
#     y = np.random.uniform(-1, 1)

#     punkt = np.sqrt(x**2 + y**2)
#     if punkt < 1:
#         x_in.append(x)
#         y_in.append(y)
#     else:
#         x_ut.append(x)
#         y_ut.append(y)


# plt.scatter(x_in,y_in, color="blue", s=10)
# plt.scatter(x_ut,y_ut, color="red", s=10)
# plt.grid(visible= True, axis= "both")
# plt.gca().set_aspect("equal")
# plt.show()




#______________________rabbit and snakes_________________



import numpy as np

def distance(x,y):
    return np.sqrt(x+y)

print(distance(0.5, 0.5))
