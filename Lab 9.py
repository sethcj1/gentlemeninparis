menu = ("Menu\n"
        "-------------\n"
        "1. Encode\n"
        "2. Decode\n"
        "3. Quit\n"
        "4. Added new menu option")


inmenu = True

def encode(string): #what was the point of writing a whole code for this
                    # we couldve just used an empty python document :(
    encoded = ""
    for i in string:
        character = int(i) +3
        encoded += str(character)
    return encoded

def decode(string):
    decoded = ""
    for i in string:
        character = int(i) -3
        decoded += str(character)
    return decoded

while inmenu:
    print(menu)
    option = input("Please enter an option: ")
    if option == "1":
        password = str(input("Please enter your password to encode: "))
        print("Your password has been encoded and stored!")
    elif option == "2":
        print(f"The encoded password is {encode(password)} and the original password is {password}")
    elif option == "3":
        exit()