items = int(input('Enter number of items: '))
cost = 0
for i in range(0, items, 1):
    price = float(input('Price of item: '))
    cost = price + cost


if cost > 100:
    cost = cost * 0.9
else:
    pass
print("Total price for " + str(items) + " items is: ${:.2f} ".format(cost))
