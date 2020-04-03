# Immutable
set1 = set([1,2,3])
print(set1)


tuple = [("First", 1), ("Second", 2), ("Third", 3)]

for i in tuple:
    print(i[0], i[1])
    print("{}: {}".format(i[0], i[1]))

def file_size(file_info):
    name, type, size = file_info
    return("{:.2f}".format(size / 1024))

print(file_size(('Class Assignment', 'docx', 17875))) # Should print 17.46
print(file_size(('Notes', 'txt', 496))) # Should print 0.48
print(file_size(('Program', 'py', 1239))) # Should print 1.21
