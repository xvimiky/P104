# x = [11,23,11,56,11,90] --> 11 is the mode

import statistics 
import pandas as pd

data = pd.read_csv("project104/project104.csv")

weight = data["Weight(Pounds)"].tolist()

mode = statistics.mode(weight)

print("Mode --> " , mode)