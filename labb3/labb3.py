import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 
import csv

# reading the data we put in
def read_data(file_path):
    data = pd.read_csv(file_path, header=None)
    return data

# seperate the data into diffrent typs
def line_separator(data):
    for x1,y1 in zip(data[0], data[1]):
        y_on_line =-1 * x1
        if y1 < y_on_line: 
            down_list.append((x1,y1,"0"))
        else:
            up_list.append((x1,y1,"1"))

# writing the data but in a separet new file
def sort_points(file_path):
    with open("labelled_data.csv", "w", newline="") as file:
        writer = csv.writer(file)
        for row in down_list:
            writer.writerow(row)
        for row in up_list:
            writer.writerow(row)

# you need to write in your own patch way in here
file_path = (r"C:\Users\stegi\Desktop\skoluppgifter\första året\programmering_kod\labb3\unlabelled_data.csv")

# my lists for seperate data points
down_list = []
up_list = []

data = read_data(file_path)
line_separator(data)
sort_points(file_path)


# getting my cordinates to plot
x1,y1,_ = zip(*up_list)
x2,y2,_ = zip(*down_list)

# my line that seperate
x_line = np.linspace(-5, 4)
y_line = -1 * x_line

# plotting fixa labels och skit imon med titel och x,y label?
plt.plot(x_line,y_line,c="red")
plt.scatter(x1,y1,c="blue",edgecolors="black")
plt.scatter(x2,y2,c="orange", edgecolors="black")
plt.show()