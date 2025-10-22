# Mh 2nd period, caeser cipher practice

# takes in if user wants to encode or decode
cipher = str(input("Would you like to encode a message, or decode a message?\n"))
cipher.lower()
cipher.strip()
message = str(input("What message would you like to encode?\n"))

# function to encode a message
def encode(message):
    # takes message and goes letter by letter shifting them by an inputed amount
    shift = int(input("How many letters should it be shifted by?\n"))
    coded = ""
    # if it's a space it leaves it
    # if it's punctiuation it leaves it
    # saves every letter in a new string
    for i in message:
        if i.isalpha():
            num = ord(i)
            num += shift
            new = chr(num)
            coded += new
        else:
            coded += i

    print(coded)
    # returns the message but shifted

# function to decode a message
def decode(message):
    # takes in an encoded message and goes letter by letter shifting them by and inputed amount
    shift  = int(input("How many places should we shift it back by\n"))
    decoded = ""
    # if it's a space it leaves it
    # if it's punctuation it leaves it
    # saves every letter in a new string
    # returns the message decoded
    for i in message:
        if i.isalpha():
            num = ord(i)
            num -= shift
            new = chr(num)
            decoded += new
        else:
            decoded += i
    
    print(decoded)

# if the user wants to encode, run the encode function
# if the user wants to decode, run the decode function
if cipher == "encode":
    encode(message)
else:
    decode(message)