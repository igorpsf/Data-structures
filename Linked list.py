class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # make None as the default value for next.


def count_nodes(head):
    # assuming that head != None
    count = 1
    current = head
    while current.next is not None:
        current = current.next
        count += 1
    return count


nodeA = Node(6) # NodeA/head with data 6
nodeB = Node(3)
nodeC = Node(4)
nodeD = Node(2)
nodeE = Node(1)

nodeA.next = nodeB
nodeB.next = nodeC
nodeC.next = nodeD
nodeD.next = nodeE

print("This linked list's length is: (should print 5)")
print(count_nodes(nodeA))   # 5
print(nodeA.data)           # 6
print(nodeA.next.data)      # 3
print(nodeA.next.next.data) # 4
print(nodeE.data)           # 1
print(nodeE.next)           # None




