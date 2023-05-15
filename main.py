import pandas as pd
import numpy as np

#Panda Config to Print all the data into the console
pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 10)
pd.set_option('display.max_rows', 3000)


# Reading the CSV file
csvFile = pd.read_csv('S2122-laliga-players.csv', header=0, usecols=['competition', 'name', 'team', 'position'])
print(csvFile)