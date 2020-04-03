# set of items, each with a key
# - insert (item): overwrite any existing key
# - delete (item)
# - search (item): return item with given key or report doesn't exist

# Python: dict
# D[key] - search
# D[key]=val - insert
# del D[key] - delete

# items = (key, value)


# for counting words
# finding common words between 2 documents
# in all databases

table = [None]*10
print(table)

def hashing_fun(x):
    return x%10

print(hashing_fun(15))  # 5
print(hashing_fun(115))  # 5

def insert(table, key, value):
    table[hashing_fun(key)] = value     # key, 0..9

insert(table, 15, 'dog')    # [None, None, None, None, None, 'dog', None, None, None, None]
print(table)

insert(table, 117, 'cat')   # [None, None, None, None, None, 'dog', None, 'cat', None, None]
print(table)

insert(table, 115, 'zebra') # [None, None, None, None, None, 'zebra', None, 'cat', None, None] , overwrite dog
print(table)

# how to avoid overwriting

table = [[] for _ in range(10)]
print(table)

def insert(table, key, value):
    table[hashing_fun(key)].append(value)

insert(table, 115, 'zebra')
print(table)

insert(table, 15, 'dog')
print(table)

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.get("model")   # Mustang
print(x)

elements = {"hydrogen": { "number": 1,
                          "weight": 1.00794,
                          "symbol": "H"},
            "helium":   { "number":2,
                          "weight": 4.002602,
                          "symbol": "He" }}

print(elements["helium"]) # {'number': 2, 'weight': 4.002602, 'symbol': 'He'}
print(elements["helium"]["weight"]) # 4.002602

##

cool_beasts = {"octopuses":"tentacles", "dolphins":"fins", "rhinos":"horns"}
for i, c in cool_beasts.items():    # .keys(), .values()
    print("{} have {}".format(i, c))

##

def email_list(domains):
    emails = []
    for mail,users in domains.items():
        for user in users:
            emails.append("{}@{}".format(user,mail))
    return(emails)

print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))


##

# The add_prices function returns the total price of all of the groceries in the dictionary. Fill in the blanks to complete this function.

def add_prices(basket):
    # Initialize the variable that will be used for the calculation
    total = 0

    # Iterate through the dictionary items
    for keys, values in basket.items():
        # Add each price to the total calculation
        # Hint: how do you access the values of
        # dictionary items?
        total += values
    # Limit the return value to 2 decimal places
	return round(total, 2)

groceries = {"bananas": 1.56, "apples": 2.50, "oranges": 0.99, "bread": 4.59,
	"coffee": 6.99, "milk": 3.39, "eggs": 2.98, "cheese": 5.44}

print(add_prices(groceries)) # Should print 28.44


# Complete the code to iterate through the keys and values of the car_prices dictionary, printing out some information about each one.

def car_listing(car_prices):
    result = ""
    for keys, values in car_prices.items():
        result += "{} costs {} dollars".format(keys, values) + "\n"
    return result

print(car_listing({"Kia Soul":19000, "Lamborghini Diablo":55000, "Ford Fiesta":13000, "Toyota Prius":24000}))