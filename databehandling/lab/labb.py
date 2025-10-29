import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt


path = r"C:\Users\stegi\Documents\github saker\python-programming-ZEBASTIAN-ANDERSSON\databehandling\lab\College.csv"

college = pd.read_csv(path, index_col=0)

college = college.rename({'Unnamed: 0': 'College'}, axis=1)
college = college.set_index('College')

print(college.info())
# print("\n\n\n")
