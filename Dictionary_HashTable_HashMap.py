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

