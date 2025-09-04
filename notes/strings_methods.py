#MH 2nd Strings methods notes

#methods
#.strip() gets rid of beginning and ending spaces
#.lower() makes the string lower case
#.upper() makes the string upper case
#.capitalize() makes first letter capital
#.title() makes first letter of every word capital
#.find() finds index of something in string
#.replace() replaces a part of a string
#.format() inserts something in place of brackets, you can also change how variables print out. This is the same as f.
age = float(input("How old? "))
name = input("What is your name? ").strip().title()
print("hello {} it's cool you're {:.3f}" .format(name, age))

print(f"hello {name} it's cool you're {age:.3f}")



#print("hello " + name)



#print(age.isdigit())

#print(age)

sentence = "the quick brown fox jumped over the lazy dog"

word = "brown"
sentence.find(word)
sentence.replace(word, "yellow")

#start = sentence.find("fox")
#length = len("fox")
#print(sentence[start: start + length])


