# Read mode
f = open("/Users/ipostnikov/Documents/Git/Data Structures/file.txt", 'r')
file_data = f.read()
f.close()   # remember to close file

print(file_data)

# Write mode

f = open("/Users/ipostnikov/Documents/Git/Data Structures/file2.txt", 'w')  # It will create file if it is not exist
f.write("Hello World!")     # append - will add text to the existing text/file
f.close()
f = open("/Users/ipostnikov/Documents/Git/Data Structures/file2.txt", 'r')  # It will create file if it is not exist
file_data2 = f.read()
f.close()

print(file_data2)


# With - automatically close file after we do something

with open("/Users/ipostnikov/Documents/Git/Data Structures/file.txt", 'r') as f:
    file_data3 = f.read()

print(file_data3)