#Mean of Elements
import pandas as pd
import csv 

data = pd.read_csv("project104/project104.csv")

new_data = data["Weight(Pounds)"].tolist()


n = len(new_data)
total = 0

for x in new_data:
     total = total + x

mean = total / n

print("Mean is : ", mean)
