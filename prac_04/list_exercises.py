# 1. Number inputs
data =[]
for numbers in range(1, 6, 1):
    number_input = int(input(f"Enter number {numbers}: "))
    data.append(number_input)
print(f"The first number is {data[0]}")
print(f"The last number is {data[-1]}")
print(f"The smallest number is {min(data)}")
print(f"The largest number is {max(data)}")
print(f"The average of the numbers is {sum(data)/5}")


# 2. Very bad security check 
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
users_username = input("Enter your username good sir: ")
if users_username in usernames:
    print("Access granted")
else:
    print("Access denied")
