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

s1 = input("Name: ")
print(s1)


names = ["Garcia", "O'Kelly", "Davis"]
print("-".join(names))