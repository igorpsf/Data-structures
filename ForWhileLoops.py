### For
for x in 1,2,3,4,5:
    print(x)

# for x in range(start, stop, step):
#    print(x)
# by default start = 0, step = 1

# for x in range(1, 101, 3):
#     print(x)

cities = ["new york city", "mountain view", "chicago", "los angeles"]
capitalized_cities = []

for city in cities:
    capitalized_cities.append(city.title())
print(capitalized_cities)

# range(start, stop-0, step-1)


### While
# x = 1
# while x < 101:
#     print(x)
#     x += 1

# x = start
# while x < stop:
# x += step

card_deck = [4, 11, 8, 5, 13, 2, 8, 10]
hand = []

while sum(hand) <= 17:
    hand.append(card_deck.pop())
print(hand)

###

manifest = [("bananas", 15), ("mattresses", 34), ("dog kennels", 42), ("machine", 120), ("cheeses", 5)]

weight = 0
items = []

for cargo in manifest:
    print("current weigh: {}".format(weight))
    if weight >= 100:
        print("breaking loop now!")
        break
    else:
        print(" adding {} ({})".format(cargo[0], cargo[1]))
        items.append(cargo[0])
        weight += cargo[1]

print(weight)
print(items)


fruit = ["orange", "strawberry", "apple"]
foods = ["apple", "apple", "hummus", "toast"]

fruit_count = 0
for food in foods:
    if food not in fruit:
        print("Not a fruit")
        continue
    fruit_count += 1
    print("Found a fruit!")

print("Total fruit: ", fruit_count)




### zip

items = ["bananas", "mattresses", "dog kennels", "machine", "cheeses"]
weights = [15, 34, 42, 120, 5]

print(list(zip(items, weights)))    # Zip

manifest2 = [("bananas", 15), ("mattresses", 34), ("dog kennels", 42), ("machine", 120), ("cheeses", 5)]

items2, weights2 = zip(*manifest2)    # unzip

print(items2)
print(weights2)



# Enumerate

items3 = ["bananas", "mattresses", "dog kennels", "machine", "cheeses"]

for i, item in enumerate(items3):
    print(i, item)

# Nested for Loops

for left in range(7):
    for right in range(left, 7):
        print("[" + str(left) + "|" + str(right) + "]", end=" ")
    print()


teams = ["Dragons", "Wolves", "Pandas", "Unicors"]
for home_team in teams:
    for away_team in teams:
        if home_team != away_team:
            print(home_team + " vs " + away_team)