import pandas as pd
import numpy as np

# Panda Config to Print all the data into the console
pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 10)
pd.set_option('display.max_rows', 3000)


def main():
    csv_file = 'S2122-laliga-santander.csv'
    print_santander(csv_file)


def print_santander(csv_file):
    # Reading the CSV file
    try:
        data = pd.read_csv(csv_file, header=0, usecols=['competition', 'name', 'team', 'position'])
        if data.empty:
            print("ERROR: CSV file is empty.")
        else:
            print(data)
    except FileNotFoundError:
        print("ERROR: CSV file '{csv_file}' not found.")
    except pd.errors.EmptyDataError:
        print("ERROR: CSV file '{csv_file}' is empty.")
    except pd.errors.ParserError:
        print("ERROR: Unable to parse CSV file '{csv_file}'.")



if __name__ == '__main__':
    main()
