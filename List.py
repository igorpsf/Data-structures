
# Mutable
A = [(1,2),(3,4),(5,6),(7,8)]

for x, y in A:
    print(x, y)

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

print(months[:6])
print(len(months))
print(months[0])
print(months[-1])
print(months[-2])  # second last, November


# in
# not in

# .len() - return how many elements in the list
# .max() - return maximum element
# .min() - return minimum element
# sorted() - return copy of the list in order smallest to largest

sizes = [15, 6, 89, 34, 65, 35]
print(sorted(sizes, reverse=True))


# List comprehensions

cities = ["new york city", "mountain view", "chicago", "los angeles"]
capitalize_cities = [city.title() for city in cities]
print(capitalize_cities)


squares = []

for x in range(9):
    squares.append(x**2)
print(squares)

squares2 = [x ** 2 for x in range(9)]
print(squares2)

squares2 = [x ** 2 for x in range(9) if x % 2 == 0]
print(squares2)

squares2 = [x ** 2 if x % 2 == 0 else x + 3 for x in range(9) ]
print(squares2)







A = [0,1,2,3,4]
s = sum(A)
m1 = min(A)
m2 = max(A)

#s1 = input("Name: ")
#print(s1)


names = ["Garcia", "O'Kelly", "Davis"]
print("-".join(names))

## Insert, Append, Remove, Pop

fruits = ["Pineapple", "Banana", "Apple", "Melon"]
fruits.append("Kiwi")
fruits.insert(0, "Orange")
fruits.remove("Pineapple")
fruits.pop(3)
fruits[0] = "Melon"

print(fruits)

# List comprehensions

multiples = [x*7 for x in range(1,11)]
print(multiples)

languages = ["Python", "Perl", "Ruby", "Go", "Java", "C"]

lenght = [len(language) for language in languages]
print(lenght)

z = [x for x in range(1, 101) if x % 3 == 0]
print(z)

# Example, "123 Main Street", "1001 1st Ave", or "55 North Center Drive". Fill in the gaps to complete this function.

def format_address(address_string):
    # Declare variables
    home_number = 0
    home_address = ''
    # Separate the address string into parts
    parts = address_string.split()

    for part in parts:
        # Determine if the address part is the
        # house number or part of the street name
        if part.isnumeric():
            home_number = part
        else:
            home_address += part + ' '
    # Does anything else need to be done
    # before returning the result?

    # Return the formatted string
    return "house number {} on street named {}".format(home_number, home_address)


print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"

print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"



## Example, highlight_word("Have a nice day", "nice") returns "Have a NICE day". Can you write this function in just one line?

def highlight_word(sentence, word):
    return " ".join([w.upper()  if word in w else w for w in sentence.split()])

print(highlight_word("Have a nice day", "nice"))
print(highlight_word("Shhh, don't be so loud!", "loud"))
print(highlight_word("Automating with Python is fun", "fun"))


##  Example, "123 Main Street", "1001 1st Ave", or "55 North Center Drive". Fill in the gaps to complete this function.

def format_address(address_string):
    # Declare variables
    home_number = 0
    home_address = ''
    # Separate the address string into parts
    parts = address_string.split()

    for part in parts:
        # Determine if the address part is the
        # house number or part of the street name
        if part.isnumeric():
            home_number = part
        else:
            home_address += part + ' '
    # Does anything else need to be done
    # before returning the result?

    # Return the formatted string
    return "house number {} on street named {}".format(home_number, home_address)


print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"

print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"