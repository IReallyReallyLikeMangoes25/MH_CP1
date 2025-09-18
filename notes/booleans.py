# MH 2nd booleans notes

# booleans are True or False
import time
import datetime as date

over = False

print(over)


name = "Mirai"
print(name.isalpha())

print(bool(name))

# Booleans are simple data types

current_time = time.time()
readable_time  =time.ctime(current_time)

print(f"Current time in seconds since January 1st of 1970 (epoch time): {current_time}")
print(f"Current time: {readable_time}")

now = date.datetime.now()
hour = now.strftime("%H")
# minutes - %M
# month number - %m
# month - %b/%B
# day - %D
# year - %Y/$y
# hour - %H
# seconds - %S

print(f"Current time according time datetime: {now}")
print(f"Hour: {hour}")
print(f"My hour variable is a string: {isinstance(hour, str)}")
print(f"My hour variable is a integer: {isinstance(hour, int)}")
print(f"My hour variable is a float: {isinstance(hour, float)}")