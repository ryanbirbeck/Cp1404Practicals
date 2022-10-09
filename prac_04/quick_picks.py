import random

numbers_each_line = 6
minimum = 1
maximum = 45

def main():
    """choose sets of random numbers"""
    num_of_quick_picks = int(input("select number of lines for quick picks: "))
    while num_of_quick_picks < 0:
        print("hmmm invalid")
        num_of_quick_picks = int(input("select number of lines for quick picks: "))

    for i in range(num_of_quick_picks):
        quickpick = []
        for j in range(numbers_each_line):
            number = random.randint(minimum, maximum)
            while number in quickpick:
                number = random.randint(minimum, maximum)
            quickpick.append(number)
        quickpick.sort()
        print(" ".join(f"{number:2}" for number in quickpick))


main()


