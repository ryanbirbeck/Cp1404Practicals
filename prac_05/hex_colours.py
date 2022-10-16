colour_name_to_code = {"ACID GREEN": "b0bf1a", "ABSOLUTE ZERO": "0048ba", "AQUA": "00ffff", "BUBBLE GUM": "ffc1cc",
                       "BURGUNDY": "800020", "CAMEO PINK": "efbbcc", "CARDINAL": "c41e3a", "CERULEAN": "007ba7",
                       "CHARCOAL": "36454f", "COBALT": "0047ab", "IRIS": "5a4fcf"}
colour = input("Enter name of a colour: ").upper()
while colour != "":
    if colour in colour_name_to_code:
        print(colour_name_to_code[colour])
    else:
        print("Invalid colour, not found in dictionary, try again,")
    colour = input("Enter name of a colour: ").upper()
