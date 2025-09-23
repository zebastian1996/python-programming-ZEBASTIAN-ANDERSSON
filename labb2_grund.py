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


#vår test data/egna input
test_data = [(25, 32),(24.2, 31.5),(22, 34),(20.5, 34)]
x,y = zip(*test_data)


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
    
    for _,slutsats in grannar[:1]:
        if slutsats == 1:
            print(f"Pikachu\n") 
            plt.scatter(test_x,test_y,c="Red", edgecolors="black", marker="X", s=60, linewidths=2)
        else:
            print(f"Pichu\n")
            plt.scatter(test_x,test_y,c="Turquoise", edgecolors="black", marker="X", s=80, linewidths=2)


plt.title("här har vi pikatchu och pitchu")
plt.xlabel("Pikachu=Röd      Pichu=Turkos      X=test data ", size=14,)
plt.scatter(pikachu_x,pikachu_y, c="red", edgecolors="black")
plt.scatter(pichu_x,pichu_y,c="Turquoise", edgecolors="black")
plt.show()



# FUNKTIONER FÖR ATT SE SCATTER? INPUT FRÅGA? KANSKE ÄVEN OM VILKEN DATA VI VILL SE? GÖRA MER FUNKTIONER?