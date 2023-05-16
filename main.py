import laliga_santander
import laliga_santander_forward
import laliga_santander_midfielder
import laliga_santander_defender
import laliga_santander_goalkeeper


def main():
    csv_file = 'S2122-laliga-santander.csv'
    # laliga_santander.print_santander(csv_file)    #Prints all of LaLiga Santander statistics unformatted
    laliga_santander_forward.print_santander_forward(
        csv_file)  # Prints all LaLiga Santander forward statistics formatted


if __name__ == '__main__':
    main()
