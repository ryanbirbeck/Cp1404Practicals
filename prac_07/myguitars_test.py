from prac_07.myguitars import Guitar


def main():
    guitars = []
    in_file = open('guitars.csv', 'r')
    for line in in_file:
        line = repr(line.strip())
        parts = line.strip().split(',')
        parts[0] = parts[0].strip("'")
        parts[2] = parts[2].strip("'")
        guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
        guitars.append(guitar)
    guitars.sort()
    in_file.close()
    for guitar in guitars:
        print(guitar)
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitar_addition = Guitar(name, year, cost)
        print(guitar_addition, "added.")
        guitars.append(guitar_addition)
        name = input("Name: ")
    out_file = open('guitars.csv', 'w')
    for guitar in guitars:
        print(guitar, file=out_file)
    out_file.close()


main()
