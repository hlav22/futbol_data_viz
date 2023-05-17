import laliga_santander
import laliga_santander_forward
import laliga_santander_midfielder
import laliga_santander_defender
import laliga_santander_goalkeeper


def main():
    csv_file = 'S2122-laliga-santander.csv'
    # laliga_santander.print_santander(csv_file)    #Prints all of LaLiga Santander statistics unformatted
    # laliga_santander_forward.print_santander_forward (csv_file)  # Prints all LaLiga Santander forward statistics formatted
    # laliga_santander_midfielder.print_santander_midfielder(csv_file)  # Prints all LaLiga Santander midfielder statistics formatted
    # laliga_santander_defender.print_santander_defender(csv_file)  # Prints all LaLiga Santander defender statistics formatted
    laliga_santander_goalkeeper.print_santander_goalkeeper(
        csv_file)  # Prints all LaLiga Santander goalkeeper statistics formatted


if __name__ == '__main__':
    main()
