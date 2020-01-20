def cylinder_volume(height, radius=5):
    pi = 3.14159
    return height * pi * radius ** 2

print(cylinder_volume(10, 7))
print(cylinder_volume(height=10, radius=7))
print(cylinder_volume(10))


# variables inside function
def word_count(document, search_term):
    """

    :param document: text document
    :param search_term: word what we want to count in document
    :return: how many times search_term in document
    """
    words = document.split()
    answer = 0
    for word in words:
        if word == search_term:
            answer += 1
    return answer

# variable outside function
ans = 10

def show_ans():
    print(ans)

show_ans()
print(ans)


# lambda
double = lambda x: x * 2
double(6)


