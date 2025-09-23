import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np

#våran kalkylator för att räkna ut alla avstånd
def kalkulator(punkt1_test_data,punkt2_känd_data):
    avståndet = np.sqrt(((punkt2_känd_data[0]-punkt1_test_data[0])**2)+((punkt2_känd_data[1]-punkt1_test_data[1])**2))
    return avståndet


#fixa här
data = pd.read_csv(r"C:\Users\stegi\Desktop\skoluppgifter\första året\programmering_kod\datapoints.txt")



# Få ut x och y till pikatchu
pikachu_data = data[data['namn'] == 1]
pikachu_x = pikachu_data["bredd"]
pikachu_y = pikachu_data["höjd"]


# Få ut x och y till pitchu
pichu_data = data[data['namn']== 0]
pichu_x = (pichu_data["bredd"])
pichu_y = (pichu_data["höjd"])


# Error hanterare
while True:
    try:
        x = float(input("skriv in x: "))
        y = float(input("skriv in y: "))
        print()
        if 0 > x or y < 0:
            print("du kan inte mata in negativ nummer så försök igen och tänk på att det behöver vara positivt")
        elif 0 == x or y == 0:
            print("har svårt att tro att den va 0cm så kontrollera nummrena och skriv om resultatet")
        else:
            plt.text(x-0.5,y+0.5,"din punkt", size=8, weight="bold")
            break
    except ValueError:
        print("text eller multiplikation av olika slag tillåts inte, va vänligen och skriv in ett positivt tal")



#vår test data/egna input
test_data = [(25, 32),(24.2, 31.5),(22, 34),(20.5, 34), (x,y)]




# kalkylerar ut vem som är närmast
for testpunkt in test_data:
    grannar = [] 
    
    #kollar emot pikachos data
    for x, y in zip(pikachu_x, pikachu_y):
        avståndet = kalkulator(testpunkt, (x, y)) 
        grannar.append((avståndet, 1))

    #kollar emot pichus data
    for x, y in zip(pichu_x, pichu_y):
        avståndet = kalkulator(testpunkt, (x,y))
        grannar.append((avståndet, 0))
    
    test_x, test_y = testpunkt
    print(f"test måtten: vikt:{test_x} höjd:{test_y} = ", end="")

    grannar.sort(key=lambda x: x[0])













    lista_pikatchu = []
    lista_pichu = []
    mängden_närmast = grannar[:10]
    distna_pika = 0
    distan_pishu = 0


    for i,slutsats in mängden_närmast:
        # print(slutsats)
        # print(i)
        if slutsats == 1:
            lista_pikatchu.append(slutsats)
            distna_pika += i
        else:
            lista_pichu.append(slutsats)
            distan_pishu += i
    # print("hejsan")
    # print(distan_pishu)
    # print("hej")
    # print(distna_pika)
    # print("hsdjfsd")

    # print(len(lista_pikatchu), "piakatchuuuuu")
    # print(len(lista_pichu), "pichu")


    if len(lista_pichu) == len(lista_pikatchu):
        print("lika många av båda nära")
        print(distan_pishu, "pishuuu")
        print(distna_pika, "pika pika yu")
        if distna_pika < distan_pishu:
            print(f"Pikachu\n") 
            plt.scatter(test_x,test_y,c="Red", edgecolors="black", marker="X", s=60, linewidths=2)
        else:
            print(f"Pichu\n")
            plt.scatter(test_x,test_y,c="Turquoise", edgecolors="black", marker="X", s=80, linewidths=2)
    elif len(lista_pikatchu) > len(lista_pichu):
        print(f"Pikachu\n") 
        plt.scatter(test_x,test_y,c="Red", edgecolors="black", marker="X", s=60, linewidths=2)
    else:
        print(f"Pichu\n")
        plt.scatter(test_x,test_y,c="Turquoise", edgecolors="black", marker="X", s=80, linewidths=2)


# plt.title("här har vi pikatchu och pitchu")
# plt.xlabel("Pikachu=Röd      Pichu=Turkos      X=test data ", size=14,)
# plt.scatter(pikachu_x,pikachu_y, c="red", edgecolors="black")
# plt.scatter(pichu_x,pichu_y,c="Turquoise", edgecolors="black")
# plt.show()


