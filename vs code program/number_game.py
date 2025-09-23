import random
import matplotlib.pyplot as plt

score_vinster = 0
score_föruster = 0

def dörrar(a,b,c,d,e):
    fel  = []
    rätt = []
    ny_lista = []

    dörr = [1,2,3]      
    kanin = (random.choice(dörr))
    if kanin in dörr:   
        dörr.remove(kanin)
        print(dörr)    
        ai = random.choice(dörr)
        rätt.append(kanin)
        print(kanin, "kaninens nr")
        if ai in dörr:
            dörr.remove(ai)
            print(dörr)
            ny_lista.append(kanin)


    if ai == kanin:
        score_vinster =+ 1
        print(f"du klarade det och har klarat det {score_vinster} många gånger")
    else:
        score_föruster =+ 1
        print("du förlorade fan va sämst du är")

dörrar(10,100,1000,10000,100000)
