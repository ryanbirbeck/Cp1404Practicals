"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""


try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
    denominator = int(input("Enter the denominator: "))
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
    print("Finished.")


# A value error will occur when the numerator and denominator values are not integers.
# using decimals or letters will result in a ValueError.

# A zero division error will occur when the denominator value is input as a zero.
# Inputting a zero will not be a value error as zero is an integer however it will be zerodivisionerror.

# The code can be changed to avoid the possibility of a ZeroDivisionError and the solution is shown in
# the while loop displayed above.
