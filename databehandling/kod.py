import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# _______________________________________________________________________________________dataframe from scratch

# data = {"Kommun": ["Malmö", "Stockholm", "Uppsala", "Göteborg"],
#         "Population": [347949, 975551, 233839, 583056]}
# df = pd.DataFrame(data)


# pop = 10379295 #totala mängden människor 

# df_gbg = df["Kommun"] == "Göteborg" # min "mask" för att få sant eller falsk för att avgöra vad som ska printas ut 
# top3 = df.sort_values("Population", ascending=False) #mask för att sortera efter värde

# top3["population (%)"] = (top3["Population"]/pop)*100 # kalkulerar ut % och tar gånger 100 för att få det i heltal istället för att 1 ska va 100% 


# print(df["Kommun"]) # A). printar ut hela colonen 
# print()
# print(df[df_gbg]) # B). kör en "mask" som jag kollar efter
# print()
# print(df.sort_values("Population", ascending=False)) # C). sortera med sort_values sen välja jag inom vilken colon man ska sorta efter och i detta fallet sorterar vi efter Population
# print()
# print(top3.head(3))# D). (head) för att bara få just den mängden
# print()
# print(top3.round(1))# E). (round) för att avrunda till 1 decimal 



#____________________________cities in sweden - real dataset______________________




path = r"C:\Users\stegi\Documents\github saker\python-programming-ZEBASTIAN-ANDERSSON\databehandling\komtopp50_2020.xlsx"

df = pd.read_excel(path, sheet_name="Totalt", header=6, usecols="A:F")
df.columns = ["Rang 2020",        "Rang 2019",    "Kommun", "Folkmängd 2020",	"Folkmängd 2019",	"Förändring"]
print(df.head())
df.info()
print("\n")
# print("\n")
print(df.sort_values("Rang 2020", ascending=False).head(5))

print("\n")
print(df["Folkmängd 2020"].sum())
print(df["Folkmängd 2019"].sum())



fig, axes = plt.subplots(1, 2, figsize=(12,5))

top5 = df.sort_values("Rang 2020").head(5)
low5 = df.sort_values("Rang 2020").tail(5)


axes[0].bar(top5["Kommun"],top5["Folkmängd 2020"])
axes[1].bar(low5["Kommun"], low5["Folkmängd 2020"])

plt.show()


#_____________________________________Cities in Sweden - gender_______________________________________________


