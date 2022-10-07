numbers = [3, 1, 4, 1, 5, 9, 2]

# numbers[0] would give the value of 3 from numbers
# numbers[-1] would give 2
# numbers[3] would give 1
# numbers[:-1] would give every number besides the position of numbers[-1], which is [3, 1, 4, 1, 5, 9]
# numbers[3:4] would give a list of numbers from position 3 to position 4, but not including position 4.
# 5 in numbers would be true
# 7 in numbers would be true
# "3" in numbers would be false as the string 3 is not in the list
# numbers + [6, 5, 3] would append 6, 5, 3 to the end of the list

numbers[0] = "ten"
numbers[-1] = 1
print(numbers[2:-1])
print(9 in numbers)


