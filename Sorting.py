### 1 Selection sort | Brute force - Locate the smallest item and put it in the first place, then the next smallest and put it in second place. From left to right.

A = [5,9,1,2,4,8,6,3,7]

def selectionsort(A):
    for i in range (0, len(A)-1):
        minIndex = i
        for j in range (i+1, len(A)):   # itterate for unsorted part of array
            if A[j] < A[minIndex]:      # If you find smaller item than minIndex
                minIndex = j            # update the index of the min element
        if minIndex != i:
            A[i], A[minIndex] = A[minIndex], A[i]   # exchange/swap elements
    return A

#print(selectionsort(A))

# asymptotic time complexity - 0(n2) - tita (O) of n square - if make input 10 times bigger, time will increase 100 times biggers



### 2 Bubble sort | swap two elements

A = [5,9,1,2,4,8,6,3,7]

def bubblesort(A):
    for i in range(0, len(A)-1):
        for j in range(0, len(A)-1-i):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
    return A

#print(bubblesort(A))

# asymptotic time complexity - 0(n2) - tita (0) of n square - performance is worst (not good to use for sorting for 1 mln numbers)


### 3 Insertion sort | Decrease-and-conquer

A = [5,9,1,2,4,8,6,3,7]

def insertionsort(A):
    for i in range(1, len(A)):
        for j in range(i-1, -1, -1):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
            else:
                break
    return A

#print(insertionsort(A))

### 4 Merge sort -

A = [5,9,1,2,8,6,3,7]

def mergesort(A):
    if len(A) <=  1:
        return
    middle = len(A)//2
    L = [A[i] for i in range(0, middle)]
    R = [A[i] for i in range(middle, len(A))]
    mergesort(L)
    mergesort(R)
    C = merge(L,R)
    for i in range(len(A)):
        A[i]=C[i]
    return A

def merge(A,B):
    C = [0] * (len(A) + len(B))
    i=k=n=0
    while i < len(A) and k < len(B):
        if A[i] <= B[k]:
            C[n] = A[i]
            i += 1
            n += 1
        else:
            C[n] = B[k]
            k += 1
            n += 1
    while i < len(A):
        C[n] = A[i]
        i += 1
        n += 1
    while k < len(B):
        C[n] = B[k]
        k += 1
        n += 1
    return C

print(mergesort(A))

# O (n log n) - the most superior running time, but taking extra memorry

### 5 Quick sort -

# O (n log n)

### 6 Heap sort -

# O (n log n)

### 7 Counting sort -

# O(n)

### 8 Radix sort -








