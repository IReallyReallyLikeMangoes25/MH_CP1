message = str(input("What message would you like to decode?\n"))
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

