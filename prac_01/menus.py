name = str(input('Enter name: '))

menu = str(input('(H)ello \n(G)oodbye \n(Q)uit \n >>> '))

while menu != 'Q':
    if menu == 'H':
        print('Hello ' + name)
    elif menu == 'G':
        print('Goodbye yellow brick road, ' + name)  # Elton John reference
    else:
        print('invalid choice')
    menu = str(input('(H) (G) (Q) \n >>> '))  # To make the command window look nicer
print('Finish him, ' + name)  # Mortal Kombat reference
