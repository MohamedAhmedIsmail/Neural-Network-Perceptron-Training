from tkinter import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap


df = pd.read_csv('N.csv')
x1=int(input("Enter the first Number: "))
x2=int(input("Enter the second Number: "))

B = df.iloc[0:150, [x1, x2]].values
plt.scatter(B[:50, 0], B[:50, 1], color='red', marker='o', label='setosa')
plt.scatter(B[50:100,0],B[50:100,1],color='blue',marker='x',label='versicolor')
plt.scatter(B[100:150,0],B[100:150,1],color='green',marker='+',label='verginica')

