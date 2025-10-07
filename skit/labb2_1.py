import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np

#våran kalkylator för att räkna ut alla avstånd
def kalkulator(punkt1_test_data,punkt2_känd_data):
    avståndet = np.sqrt(((punkt2_känd_data[0]-punkt1_test_data[0])**2)+((punkt2_känd_data[1]-punkt1_test_data[1])**2))
    return avståndet


#fixa här
data = pd.read_csv(r"C:\Users\stegi\Desktop\skoluppgifter\första året\programmering_kod\datapoints2.txt")


# Få ut x och y till pikatchu
pikachu_data = data[data[' label (0-pichu'] == 1]
pikachu_x = pikachu_data["(width (cm)"]
pikachu_y = pikachu_data[" height (cm)"]


# Få ut x och y till pitchu
pichu_data = data[data[' label (0-pichu']== 0]
pichu_x = (pichu_data["(width (cm)"])
pichu_y = (pichu_data[" height (cm)"])


print("skriv nu in dina mått")
# Error hanterare
while True:
    try:
        x = int(input("skriv in berdd: "))
        y = int(input("skriv in höjd: "))
        print()
        if 0 > x or y < 0:
            print("du kan inte mata in negativ nummer så försök igen och tänk på att det behöver vara positivt")
        elif 0 == x or y == 0:
            print("har svårt att tro att den va 0cm så kontrollera nummrena och skriv om resultatet")
        else:
            break
    except ValueError:
        print("text eller multiplikation av olika slag tillåts inte, va vänligen och skriv in ett positivt tal")



#vår test data/egna input
test_data = [(25, 32),(24.2, 31.5),(22, 34),(20.5, 34), (x,y)]
x,y = zip(*test_data)









# kalkylerar ut vem som är närmast
for testpunkt in test_data:
    grannar_pikachu = []
    grannar_pichu = [] 
    
    #kollar emot pikachos data
    for x, y in zip(pikachu_x, pikachu_y):
        avståndet = kalkulator(testpunkt, (x, y)) 
        grannar_pikachu.append((avståndet))

    #kollar emot pichus data
    for x, y in zip(pichu_x, pichu_y):
        avståndet = kalkulator(testpunkt, (x,y))
        grannar_pichu.append((avståndet, 0))
    
    
    test_x, test_y = testpunkt
    print(f"test måtten: bred:{test_x} höjd:{test_y} = ", end="")

    print("hejsa")
    print(sum.grannar_pikatchu)
    print(sum.grannar_pichu)
    print("hejdå")

#     if sum_avstånd[1] > sum_avstånd[0]:
#         print("Pikachu\n") 
#         plt.scatter(test_x,test_y,c="Red", edgecolors="black", marker="X", s=60, linewidths=2)
#     else:
#         print("Pichu\n")
#         plt.scatter(test_x,test_y,c="Turquoise", edgecolors="black", marker="X", s=80, linewidths=2)



# plt.title("här har vi pikatchu och pitchu")
# plt.xlabel("Pikachu=Röd      Pichu=Turkos      X=test data ", size=14,)
# plt.scatter(pikachu_x,pikachu_y, c="red", edgecolors="black")
# plt.scatter(pichu_x,pichu_y,c="Turquoise", edgecolors="black")
# plt.show()
