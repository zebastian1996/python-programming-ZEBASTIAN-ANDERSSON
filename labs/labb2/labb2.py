import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np

#kollar avstånd 
def kalkulator(test_data,känd_data):
    return np.sqrt(((känd_data[0]-test_data[0])**2)+((känd_data[1]-test_data[1])**2))

# separerar datan
def sortera_data(datan):
    nya = np.array(datan)
    for data_points in nya:
        if 0 in data_points[2:3]:
            pichu.append(data_points[0:2])
        else:
            pikachu.append(data_points[0:2])

# tar in dom kända data punkterna
data = pd.read_csv(r"C:\Users\frolu\OneDrive\Skrivbord\skol kodning\labb2\datapoints.txt")

# Error hanterare / här vi skriver in input   
while True:
    try:          
        x = 27 #x = float(input("skriv in bredd: "))
        y = 32 #y = float(input("skriv in höjd: "))
        if 0 > x or y < 0:
            print("du kan inte mata in negativ nummer så försök igen och tänk på att det behöver vara positivt")
        elif 0 == x or y == 0:
            print("har svårt att tro att den va 0cm så kontrollera nummrena och skriv om resultatet")
        else:
            plt.text(x-0.5,y+0.5,"din punkt", size=8, weight="bold")
            break
    except ValueError:
        print("text eller multiplikation av olika slag tillåts inte, va vänligen och skriv in ett positivt tal")

# samling och sortering av test,pichu och pikachu data
test_data = [(25, 32),(24.2, 31.5),(22, 34),(20.5, 34), (x,y)]
pichu = []
pikachu = []
sortera_data(data)

for xTest,yTest in test_data:
    grannar = []
    for i in pichu:
        grannar.append(((kalkulator((xTest,yTest), i)),0))
    for i in pikachu:
        grannar.append(((kalkulator((xTest,yTest), i)), 1))

    # lista samt distans som en backup om dom är likanära för att få bästa resultatet 
    mängd_pikachu= []
    mängd_pichu = []
    distna_pikachu = 0
    distan_pishu = 0 

    grannar.sort(key=lambda x: x[0])
    for i,granne in grannar[0:10]:
        if granne == 1:
            mängd_pikachu.append(granne)
        else:
            mängd_pichu.append(granne)

    # kollar vem som är närmast och avgör vilken titel den får
    if len(mängd_pikachu) == len(mängd_pichu):
        if distna_pikachu < distan_pishu:
           print(f"det blev en pikachu")
           plt.scatter(xTest,yTest,c="red", edgecolors="black", marker="X", s=95)
        else:
            print(f"det blev en pichu")
            plt.scatter(xTest,yTest,c="blue", edgecolors="black", marker="X",s=95) 
            
    elif len(mängd_pikachu) > len(mängd_pichu):
        print(f"det blev en pikachu")
        plt.scatter(xTest,yTest,c="red", edgecolors="black", marker="X", s=95)
    else:
        print(f"det blev en pichu")
        plt.scatter(xTest,yTest,c="blue", edgecolors="black", marker="X",s=95)

# skapar kordinaterna och plottar
x,y=zip(*pichu)
x1,y1=zip(*pikachu)

plt.scatter(x,y,c="blue", edgecolors="black")
plt.scatter(x1,y1,c="red", edgecolors="black")
plt.title("röd = pikachu            blå = pichu            x = testpunkter")
plt.show() 