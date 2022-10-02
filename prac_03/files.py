# a
namefile = open('name.txt', 'w')
name = input("Enter your name: ")
print(name, file=namefile)
namefile.close()


# b
namefile = open('name.txt', 'r')
read_name = (namefile.read().strip())
print(f"Your name is {read_name}")
namefile.close()
# I was having trouble with this question because I thought that I had to print the
# name back into the name file, but the solution didn't do that, so it's all good.

# c
numberfile = open('numbers.txt', 'r')
first_number = int(numberfile.readline())
second_number = int(numberfile.readline())
print(first_number + second_number)
numberfile.close()


# d
numberfile = open('numbers.txt', 'r')
total = 0
for line in numberfile:
    number_on_line = int(line)
    total = number_on_line + total
print(total)
numberfile.close()

