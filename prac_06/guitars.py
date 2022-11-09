
from prac_06.guitar import Guitar


def main():
    guitars = []
    print("My guitars!")
    # name = input("Name: ")
    # while name != "":
    #     year = int(input("Year: "))
    #     cost = float(input("Cost: "))
    #     guitar_addition = Guitar(name, year, cost)
    #     print(guitar_addition, "added.")
    #     guitars.append(guitar_addition)
    #     name = input("Name: ")

    guitars.append(Guitar("L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 jtv-59", 2000, 5050.90))

    if guitars:
        guitars.sort()
        print("These are the guitars:")
        for i, guitar in enumerate(guitars, 1):
            vintage = ""
            if guitar.is_vintage():
                vintage = " (vintage)"
            print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage}")
    else:
        print("No guitars sorry")


main()
