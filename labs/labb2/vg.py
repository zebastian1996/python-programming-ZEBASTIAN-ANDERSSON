import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np
import random as rnd
#kollar avstånd 
def kalkulator(test_data,känd_data):
    return np.sqrt(((känd_data[0]-test_data[0])**2)+((känd_data[1]-test_data[1])**2))
     
# separerar datan
def sortera_data(datan):
    nya = np.array(datan)
    for data_points in nya:
        posistion = tuple(data_points[0:2])
        if 0 in data_points[2:3]:
            pichu.append(posistion)
        else:
            pikachu.append(posistion)

# tar in dom kända data punkterna
data = pd.read_csv(r"C:\Users\stegi\Documents\github saker\python-programming-ZEBASTIAN-ANDERSSON\labs\labb2\datapoints2.txt")

# här skapar vi listor sen shufflar och delar upp dom
pichu = []
pikachu = []

accuracys = []
sortera_data(data)

for u in range(10):
    # sufflar listorna och direkt efter delar jag upp listorna i träningsdata/test
    rnd.shuffle(pichu)
    rnd.shuffle(pikachu)
    
    träning_pikachu, test_pikachu = pikachu[:50], pikachu[50:]
    träning_pichu, test_pichu =  pichu[:50], pichu[50:]
    
    rätt = 0
    fel = 0

    for testpunkt in test_pichu+test_pikachu:
        grannar = []
        # här skapar vi ett facit 
        if testpunkt in test_pikachu:
            facit = 1
        else: 
            facit = 0
        
        for i in träning_pichu:
            grannar.append((kalkulator(testpunkt , i), 0))
        for i in träning_pikachu:
            grannar.append((kalkulator(testpunkt , i), 1))

        mängd_pikachu= []
        mängd_pichu = []
        distna_pika = 0
        distan_pishu = 0 
        
        grannar.sort(key=lambda x: x[0])

        for längd,granne in grannar[0:10]:
            if granne == 1:
                mängd_pikachu.append(granne)
                distna_pika += längd
            else:
                mängd_pichu.append(granne)
                distan_pishu += längd

        # óm det är lika många så kollar vi distansen istället
        if len(mängd_pikachu) == len(mängd_pichu): 
            if distna_pika < distan_pishu:
                gissning = 1
            else:
                gissning = 0
   
        # här drar vi vår gissning
        else:
            if len(mängd_pikachu) > len(mängd_pichu):
                gissning = 1
            else:
                gissning = 0

        # kontrollerar svaret
        if gissning == facit:
            rätt += 1
        else:
            fel += 1
    #rättar resultatet
    acc = rätt / (rätt + fel)
    accuracys.append(acc)

print(f"testet resulterade i {np.mean(accuracys):.2f}% accuracies")
plt.ylim(0,1)
plt.xlim(0,10)
plt.plot(accuracys)
plt.grid()
plt.show()