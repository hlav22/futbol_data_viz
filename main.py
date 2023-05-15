import pandas as pd
import laliga_santander_forward


def main():
    csv_file = 'S2122-laliga-santander.csv'
    # print_santander(csv_file)
    laliga_santander_forward.print_santander_forward(csv_file)


if __name__ == '__main__':
    main()
