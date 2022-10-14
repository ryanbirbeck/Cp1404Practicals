import random
# print(random.randint(5, 20))  # line 1
# print(random.randrange(3, 10, 2))  # line 2
# print(random.uniform(2.5, 5.5))  # line 3

"""What did you see on line 1?"""
# On line 1, I saw that the line produced a random integer
# in the range of 5 to 20, inclusive


# On line 2, I saw that the line produced a random number inside the range of 3 to 10,
# however, the random number was every second number from 3 to 10, due to the 2.
# Line 2 could not have produced a 4, as 4 is an even number and the line goes up in multiples of 2.
# The smallest number possible is 3


# On line 3, I saw that the code produced a random number in the range from 2.5 to 5.5
# the 'random number' produced had a maximum of 16 decimal places which I can infer means that
# the random number is found anywhere on a uniform gradient line from 2.5 to 5.5
# The smallest number I could have seen would be 2.5

print(random.randint(1, 100))


