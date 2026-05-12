# Basic
from collections import deque
q=deque()
q.append(2)
q.append(3)
q.append(3)

# print(q.popleft())

# print(q)

#  q  1 --> Print Front Element
print("Front element :",q[0])

# q 2 --> Print Rear Element
print("Rear elemenr:",q[-1])

# Q 3 -->Check Queue Empty
def check_queue(q):
    
    
    if len(q)==0:
        return "Empty"
    else:
        return "Not empty"
    
q=deque()
q.append(2)
print(check_queue(q))