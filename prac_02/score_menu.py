def main():
    menu = str(input("(I)nput score:\n(P)rint stars:\n(Q)uit:\n>>")).upper()
    while menu != "Q":
        if menu == "I":
            points = int(input("Input your score: "))
            points, result = assign_result_to_score(points)
            print("Your score is " + result)
            menu = str(input("(I)nput score:\n(P)rint stars:\n(Q)uit:\n>>")).upper()
        elif menu == "P":
            print_stars(points)
            menu = str(input("(I)nput score:\n(P)rint stars:\n(Q)uit:\n>>")).upper()
        elif menu == "Q":
            print("goodbye")
            menu = str(input("(I)nput score:\n(P)rint stars:\n(Q)uit:\n>>")).upper()
        else:
            print("invalid")
            menu = str(input("(I)nput score:\n(P)rint stars:\n(Q)uit:\n>>")).upper()


def assign_result_to_score(points):
    while points < 0 or points > 100:
        print("Invalid score")
        points = int(input("Input your score: "))
    if points >= 90:
        result = "excellent"
    elif points >= 50:
        result = "passable"
    else:
        result = "bad"
    return points, result


def print_stars(points=1, shape='*'):
    print(shape * points)


main()

