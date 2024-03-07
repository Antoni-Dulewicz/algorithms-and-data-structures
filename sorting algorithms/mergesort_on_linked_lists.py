from typing import List
class Node:
    def __init__(self,value,next = None):
        self.value = value
        self.next = next

def make_list(tab: List)->Node:
    lst = Node(tab[0])
    tmp = lst

    for i in range(1,len(tab)):
        tmp.next = Node(tab[i])
        tmp = tmp.next

    return lst    

def print_list(lst: Node):
    while lst is not None:
        print(lst.value,end=" -> ")
        lst = lst.next
    print("|")    
    return


def merge_lists(lst1: Node, lst2: Node)-> Node:
    if lst1 is None:
        return lst2
    if lst2 is None:
        return lst1

    if lst1.value <= lst2.value:
        lst_res = lst1
        lst1 = lst1.next
    else:
        lst_res = lst2
        lst2 = lst2.next
        
    lst_res.next = None
    lst_res_head = lst_res

    while lst1 is not None and lst2 is not None:
        if lst1.value <= lst2.value:
            lst_res.next = lst1
            lst1 = lst1.next
            
        else:
            lst_res.next = lst2
            lst2 = lst2.next
        
        lst_res = lst_res.next
        lst_res.next = None
    
    if lst1 is None:
        lst_res.next = lst2
    else:
        lst_res.next = lst1
    
    return lst_res_head

def separate(lst: Node)-> tuple[Node,Node]:
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

def merge_sort(lst: Node)->Node:
    while True:
        lst_res = Node(None)
        tail = lst_res
        cnt = 0
        while lst is not None:
            
            block1,lst = separate(lst)
            
            block2,lst = separate(lst)
            
            tail.next = merge_lists(block1,block2)
            
            while tail.next is not None:
                tail = tail.next
            cnt += 1
        if cnt == 1:
            return lst_res.next
        
        
        lst = lst_res.next

lst1 = make_list([2,4,7,9,11])
lst2 = make_list([1,3,5,8,10,14,21])
lst = make_list([5,2,7,1,8,14,4,10,2,14])
lst_t = make_list([1,8,4,10,2,14])

lst = merge_sort(lst)
print_list(lst)