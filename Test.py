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

print(insertionsort(A))