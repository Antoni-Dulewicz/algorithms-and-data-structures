from typing import List
class Node:
    def __init__(self,value,next = None):
        self.value = value
        self.next = next

def makeList(T: List[int])->Node:
    lst = Node(T[0])
    curr = lst

    for i in range(1,len(T)):
        curr.next = Node(T[i])
        curr = curr.next
    return lst

def printList(lst: Node)->Node:
    while lst is not None:
        print(lst.value,end=", ")
        lst = lst.next
    print("") 

def rotateList(lst: Node)->Node:
    if lst is None:
        return
    curr = lst
    prev = None
    while curr is not None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev

lst = makeList([4,5,2,1,4])
lst = rotateList(lst)
printList(lst)