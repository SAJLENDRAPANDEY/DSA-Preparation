# # Basic
from collections import deque
# q=deque()
# q.append(2)
# q.append(3)
# q.append(3)

# # print(q.popleft())

# # print(q)

# #  q  1 --> Print Front Element
# print("Front element :",q[0])

# # q 2 --> Print Rear Element
# print("Rear elemenr:",q[-1])

# # Q 3 -->Check Queue Empty
# def check_queue(q):
    
    
#     if len(q)==0:
#         return "Empty"
#     else:
#         return "Not empty"
    
# q=deque()
# q.append(2)
# print(check_queue(q))



# Q -- 4 -->Count Elements in Queue
# def count_ele(q):
#     count=0
#     for i in q:
#         count+=1
#     return count
# q=deque()
# q.append(2)
# print(count_ele(q))


# Q 5 --> Reverse Queue
# from collections import deque
# def reverse_q(q):
#     res=[]
#     while q:
#         res.append(q.pop())
#     return res
# q=deque()
# q.append(1)
# q.append(2)
# print(reverse_q(q))


# Q 6 --> Find Maximum Element
# from collections import deque
# def max_ele(q):
#     max_el=0
#     while q:
#         value=q.pop()
#         if max_el<value:
#             max_el=value
#     return max_el
# q=deque()
# q.append(2)
# q.append(4)
# print(max_ele(q))



# Q  7 --> Sum of Queue Elements
# from collections import deque
# def sum_q(q):
#     sum=0
#     for i in q:
#         sum+=i
#     return sum
# q=deque()
# q.append(2)
# q.append(4)
# print(sum_q(q))



# Q 8 --> Generate Binary Numbers using Queue
# def generate_bin(n):
#     q=deque()
#     q.append("1")
#     for i in range(n):
#         front=q.popleft()
#         print(front)

#         q.append(front+"0")
#         q.append(front+"1")
# generate_bin(5)



# Q 9 --> leetcode 682 
def calPoints(operations):

    stack = []

    for op in operations:

        if op == "+":
            stack.append(stack[-1] + stack[-2])

        elif op == "D":
            stack.append(2 * stack[-1])

        elif op == "C":
            stack.pop()

        else:
            stack.append(int(op))

    return sum(stack)


operations = ["5", "2", "C", "D", "+"]
print(calPoints(operations))