from prac_06.guitar import Guitar

CURRENT_YEAR = 2022


def run_tests():
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40

    guitar = Guitar(name, year, cost)
    other = Guitar("Another Guitar", 2002, 3000)

    print(f"{guitar.name} get_age() - Expected 100. Got {guitar.get_age()}")
    print(f"{other.name} get_age() - Expected 20. Got {other.get_age()}")
    print(f"{guitar.name} is_vintage() - Expected True. Got {guitar.is_vintage()}")
    print(f"{other.name} is_vintage() - Expected False. Got {other.is_vintage()}")


run_tests()
