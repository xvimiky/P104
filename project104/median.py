#Median of Elements

import pandas as pd
import csv 

data = pd.read_csv("project104/project104.csv")

new_data = data["Weight(Pounds)"].tolist()


new_data.sort()

# Getting the median

n = len(new_data)
total = 0

if n % 2 == 0:
    #First Middle Number
    median1 = float(new_data[n//2])

    #Second Middle Number
    median2 = float(new_data[n//2 - 1])

    #Mean of two numbers
    median = (median1 + median2) / 2

else:
    median = new_data[n//2]

print("Median is : ", median)
