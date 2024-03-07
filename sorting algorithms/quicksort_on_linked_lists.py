from typing import List
class Node:
    def __init__(self,value,next = None):
        self.value = value
        self.next = next

def print_list(lst: Node):
    while lst is not None:
        print(lst.value,end=" -> ")
        lst = lst.next
    print('|')

def make_list(tab: List)->Node:
    lst = Node(tab[0])
    curr = lst
    for i in range(1,len(tab)):
        curr.next = Node(tab[i])
        curr = curr.next
    return lst

def separate(lst: Node)->tuple[Node:Node]:
    if lst is None:
        return None,None
    curr = lst
    while curr.next is not None:
        if curr.value > curr.next.value:
            tmp = curr.next
            curr.next = None
            return lst,tmp
        curr = curr.next
    return lst,None

def partition(lst: Node)->Node:
    if lst is None:
        return None
    curr = lst
    while curr is not None:
        block1,block2 = separate(lst)
        pivot = block2
        block2 = block2.next
        pivot.next = None


lst = make_list([5,4,2,7,8,2])
print_list(lst)
