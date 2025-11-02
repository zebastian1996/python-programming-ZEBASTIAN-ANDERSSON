import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt


path = r"C:\Users\stegi\Documents\github saker\python-programming-ZEBASTIAN-ANDERSSON\databehandling\lab\College.csv"

college = pd.read_csv(path)

college = college.rename({'Unnamed: 0': 'College'}, axis=1)
#college = college.set_index('College')

print(college)
# print("\n\n\n")

