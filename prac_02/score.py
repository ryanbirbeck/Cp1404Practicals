import random


def main():
    """assign a result to a score"""
 # points = getuserscore()
    points = findrandomscore()
    print("Your score is " + str(points))
    if points < 0 or points > 100:
        result = "Invalid score"
    elif points >= 90:
        result = "Excellent"
    elif points >= 50:
        result = "Passable"
    else:
        result = "Bad"
    print("Your score is " + result)


# def getuserscore():
"""ask the user to input their own score"""
#     points = float(input("Enter score: "))
#     return points


def findrandomscore():
    """find a random score"""
    points = random.randint(0, 100)
    return points


main()
