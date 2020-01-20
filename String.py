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

