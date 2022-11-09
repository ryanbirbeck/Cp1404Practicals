from prac_07.myguitars import Guitar


def main():
    guitars = []
    in_file = open('guitars.csv', 'r')
    for line in in_file:
        parts = line.strip().split(',')
        guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
        guitars.append(guitar)
    in_file.close()



    #
    # for i, guitar in enumerate(guitars):
    #     if Guitar.__lt__(guitar, i + 1):
    #         print(guitar)


main()
