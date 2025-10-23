# Mh 2nd period, caeser cipher practice

# takes in if user wants to encode or decode
cipher = str(input("Would you like to encode a message, or decode a message?\n"))
cipher.lower()
cipher.strip()

# function to encode a message
def encode(message):
    # takes message and goes letter by letter shifting them by an inputed amount
    shift = int(input("How many letters should it be shifted by?\n"))
    coded = ""
    # checks if the shift goes past z
    # if it does it goes back to a
    # saves every letter in a new string
    for i in message:
        if i.isalpha():
            if i.isupper():
                num = ord(i) - 65
                shift = shift % 26
                if (num + shift) > 25:
                    num -= 26
                num += shift
                new = chr(num + 65)
                coded += new
            else:
                num = ord(i) - 97
                shift = shift % 26
                if (num + shift) > 25:
                    num -= 26
                num += shift
                new = chr(num + 97)
                coded += new
        else:
            coded += i
    # adds on every letter to an empty string
    print(coded)
    # returns the message but shifted

# function to decode a message
def decode(message):
    # takes in an encoded message and goes letter by letter shifting them by an inputed amount
    shift  = int(input("How many places should we shift it back by\n"))
    decoded = ""
    # checks if after shifting the letter goes past a
    # if it does it goes back to z
    # saves every letter in a new string
    for i in message:
        if i.isalpha():
            if i.isupper():
                num = ord(i) - 65
                shift = shift % 26
                if (num - shift) < 0:
                    num += 26
                num -= shift
                new = chr(num + 65)
                decoded += new
            else:
                num = ord(i) - 97
                shift = shift % 26
                if (num - shift) < 0:
                    num += 26
                num -= shift
                new = chr(num + 97)
                decoded += new
        else:
            decoded += i
    # adds on every letter to an empty string
    print(decoded)
    # returns message but decoded

# if the user wants to encode, run the encode function
# if the user wants to decode, run the decode function
if cipher == "decode":
    decode(str(input("What message would you like to decode?\n")))
elif cipher == "encode":
    encode(str(input("What message would you like to encode?\n")))
else:
    print("That is not a valid input.")