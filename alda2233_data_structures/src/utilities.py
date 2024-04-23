'''
Created on Jan 14, 2024

Author:  Mohamed Aldakhil
ID:      169072233
Email:   alda2233@mylaurier.ca
__updated__ = '2024-01-12'
'''

from Stack_array import Stack
from Queue_array import Queue
from Priority_Queue_array import Priority_Queue

def array_to_stack(stack, source):
    """
    -------------------------------------------------------
    Pushes contents of source onto stack. At finish, source is empty.
    Last value in source is at bottom of stack,
    first value in source is on top of stack.
    Use: array_to_stack(stack, source)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    
   
    n=len(source)
    i=n-1

    while i>=0:
        stack.push(source[i])
        i-=1
    
    source.clear()
    return None




def stack_to_array(stack, target):
    """
    -------------------------------------------------------
    Pops contents of stack into target. At finish, stack is empty.
    Top value of stack is at end of target,
    bottom value of stack is at beginning of target.
    Use: stack_to_array(stack, target)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """

    while not stack.is_empty():
        target.append(stack.pop())
    target.reverse()
    return None



def stack_test(source):
    """
    -------------------------------------------------------
    Tests the methods of Stack for empty and
    non-empty stacks using the data in source:
    is_empty, push, pop, peek
    (Testing pop and peek while empty throws exceptions)
    Use: stack_test(source)
    -------------------------------------------------------
    Parameters:
        source - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    
    stack=Stack()
    empty=stack.is_empty()
    print(f"is empty: {empty}")
    
    stack.push(source[0])
    print(f"pushed {source[0]}")
    
    empty=stack.is_empty()
    print(f"is empty: {empty}")
    
    value = stack.peek()
    print(f"peek: {value}")
    
    for i in stack:
        print(f"Stack: {i}")
        
    stack.push(source[1])
    print(f"pushed {source[1]}")
    
    for i in stack:
        print(f"Stack: {i}")
    
    while not stack.is_empty():
        remove=stack.pop()
        print(f"removed {remove}")
    
    print("empty stack")
    empty=stack.is_empty()
    print(f"is empty: {empty}")
    

    return None
























def array_to_queue(queue, source):
    """
    -------------------------------------------------------
    Inserts contents of source into queue. At finish, source is empty.
    Last value in source is at rear of queue,
    first value in source is at front of queue.
    Use: array_to_queue(queue, source)
    -------------------------------------------------------
    Parameters:
        queue - a Queue object (Queue)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
   
    for i in source:
        queue.insert(i)
    source.clear()
    return None

def queue_to_array(queue, target):
    """
    -------------------------------------------------------
    Removes contents of queue into target. At finish, queue is empty.
    Front value of queue is at front of target,
    rear value of queue is at end of target.
    Use: queue_to_array(queue, target)
    -------------------------------------------------------
    Parameters:
        queue - a Queue object (Queue)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    
   
    while not queue.is_empty():
        value=queue.remove()
        target.append(value)
       
    
    return None

def queue_test(a):
    """
    -------------------------------------------------------
    Tests queue implementation.
  Tests the methods of Queue are tested for both empty and
  non-empty queues using the data in a:
        is_empty, insert, remove, peek, len
    Use: queue_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    q = Queue()

    
    empty= q.is_empty()
    print(f"is empty {empty}")
    
    q.insert(a[0])
    print(f"inserted {a[0]}")
    empty= q.is_empty()
    print(f"is empty {empty}")
    
    value = q.peek()
    print(f"peek: {value}")
    
    q.insert(a[1])
    print(f"inserted {a[1]}")
    
    n = len(q)
    print(f"length: {n}")
    
    while not q.is_empty():
        remove = q.remove()
        print(f"removed {remove}")
        
    empty= q.is_empty()
    print(f"is empty {empty}")
    
    n = len(q)
    print(f"length: {n}")
    
    return None
    
    
     
     
     
     
 
   
   
   
   
   
   
   
   
   
   
   
   
   
   
def array_to_pq(pq, source):
    """
    -------------------------------------------------------
    Inserts contents of source into pq. At finish, source is empty.
    Last value in source is at rear of pq,
    first value in source is at front of pq.
    Use: array_to_pq(pq, source)
    -------------------------------------------------------
    Parameters:
        pq - a Priority_Queue object (Priority_Queue)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    
    for i in source:
        pq.insert(i)
    
    source.clear()
    
    return None

def pq_to_array(pq, target):
    """
    -------------------------------------------------------
    Removes contents of pq into target. At finish, pq is empty.
    Highest priority value in pq is at front of target,
    lowest priority value in pq is at end of target.
    Use: pq_to_array(pq, target)
    -------------------------------------------------------
    Parameters:
        pq - a Priority_Queue object (Priority_Queue)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    
    while not pq.is_empty():
        value = pq.remove()
        target.append(value)
        
    return None

def priority_queue_test(a):
    """
    -------------------------------------------------------
    Tests priority queue implementation.
    Test the methods of Priority_Queue are tested for both empty and
    non-empty priority queues using the data in a:
        is_empty, insert, remove, peek
    Use: priority_queue_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    pq = Priority_Queue()



    
    empty= pq.is_empty()
    print(f"is empty {empty}")
    
    pq.insert(a[0])
    print(f"inserted {a[0]}")
    empty= pq.is_empty()
    print(f"is empty {empty}")
    
    value = pq.peek()
    print(f"peek: {value}")
    
    pq.insert(a[1])
    print(f"inserted {a[1]}")
    
    n = len(pq)
    print(f"length: {n}")
    
    while not pq.is_empty():
        remove = pq.remove()
        print(f"removed {remove}")
        
    empty= pq.is_empty()
    print(f"is empty {empty}")
    
    n = len(pq)
    print(f"length: {n}")
    
    return None

   

















from List_array import List





def array_to_list(llist, source):
    """
    -------------------------------------------------------
    Appends contests of source to llist. At finish, source is empty.
    Last element in source is at rear of llist,
    first element in source is at front of llist.
    Use: array_to_list(llist, source)
    -------------------------------------------------------
    Parameters:
        llist - a List object (List)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    
    while len(source) > 0:
        llist.append(source.pop(0))
    return None
    
    
    
    return None

def list_to_array(llist, target):
    """
    -------------------------------------------------------
    Removes contents of llist into target. At finish, llist is empty.
    Front element of llist is at front of target,
    rear element of llist is at rear of target.
    Use: list_to_array(llist, target)
    -------------------------------------------------------
    Parameters:
        llist - a List object (List)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """

    while not llist.is_empty():
        target.append(llist.pop(0))
    return None








from Food import Food



def list_test(source):
    """
    -------------------------------------------------------
    Tests List implementation.
    The methods of List are tested for both empty and
    non-empty lists using the data in source
    Use: list_test(source)
    -------------------------------------------------------
    Parameters:
        source - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    lst = List()

  
    print("empty",lst.is_empty())
    lst.append(source[0])
    print(" empty false now:",lst.is_empty())
    print()
    print("append and peek the value", lst.peek())
    print()
    lst.append(source[1])
    lst.insert(0,source[2])
    print("insert a food at index 0")
    print()
    for v in lst:
        print(v)
    print()
    print("What is the maximum food?",lst.max())
    print()
    print("What is the minimum food?",lst.min())
    print()
    key = Food("Spring rolls wrong", 2, True, 653)
    print("find any instances spring rolls wrong:")
    print("does it contain key?",key in lst)
    print("how many times?",lst.count(key))
    
    r = lst.remove(key)
    print("remove spring rolls wrong",r)
    print()
    lst[1] = Food("Chickie Nuggies",1,False,66)
    hmm = lst[0]
    print("update the list at index 1")
    print("the first variable in the list is",hmm)
    for v in lst:
        print(v)
    n = lst.index(Food("Chickie Nuggies",1,False,66))
    print("the index Chickie Nuggies is",n)
    print()
    print("finding chickie nuggies...")
    print(lst.find(Food("Chickie Nuggies",1,False,66)))
    
    return

 



        
    
    
    
    
    