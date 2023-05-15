import pandas as pd

# Reading the CSV file
csvFile = pd.read_csv("S2122-laliga-players.csv", header=0, usecols=["competition", "name", "position"])
print(csvFile)