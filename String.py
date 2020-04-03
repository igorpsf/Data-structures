#Immutable

# s = "Hello"
# print(s.find("lo")) # 3
#
# s2 = """Hello1
# Hello2
# Hello3
# """
# print(s2)
#
# x = s.count("l")
# print(x)    # 2
#
# s = "AAAAAA"
# s.replace("AAA", "BB")
# print(s)    # AAAAAA

s = "Hello"

print(s[0])     # H
print(s[-5])    # H
print(s[::-1])  # olleH

#S[start:stop:step]

s = "abcdefgh"
x = s
s = s[::2] + s[::-2]
print(s)    # aceghfdb

d = "Hello"
print(d[::2])

s = "My \n" \
    "name \n" \
    "is"
print(s)

s2 = """My
name
is"""
print(s2)

# strip(), lstrip(), rstrip()

print("  hi  ".strip()) # hi

# isnumeric()

print("1234".isnumeric())   # True

# format

name = "Manny"
number = len(name) * 3
print("Your lucky number is {number}, {name}".format(name=name, number=len(name)*3))

first = "apple"
second = "banana"
third = "carrot"

formatted_string = "{0} {2} {1}".format(first, second, third)

print(formatted_string)


#

price = 7.5
with_tax = price * 1.09
print("Base price: ${:.2f}. With Tax: ${:.2f}".format(price, with_tax))

def to_celcius(x):
    return (x-32)*5/9

for x in range(0, 101, 10):
    print("{:>3} F | {:6.2f} C".format(x, to_celcius(x)))

