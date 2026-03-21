# # class queue:
# #     def __init__(self):
# #         self.q=[]
# #     def enqueue(self,val):
# #         self.q.append(val)
# #     def dequeue(self):
# #         if not self.is_empty():
# #             return self.q.pop(0)
# #         return "queue is empty"
# #     def is_empty(self):
# #         return len(self.q)==0
# #     def front(self):
# #         if not self.is_empty():
# #             return self.q[0]
# #         else:
# #             return None
# #     def rear(self):
# #         if not self.is_empty():
# #             return self.q[-1]
# #         else:
# #             return None
# # q=queue()
# # q.enqueue(3)
# # q.enqueue(5)
# # q.enqueue(7)
# # q.enqueue(9)
# # print(q.dequeue())
# # print(q.front())
# # print(q.rear())


# # Question 2 --> Reverse a queue.
# # class queue:
# #     def __init__(self):
# #         self.q=[]
# #     def enqueue(self,val):
# #         self.q.append(val)
# #     def dequeue(self):
# #         if not self.is_empty():
# #             return self.q.pop(0)
# #         return "Queue is empty"
# #     def is_empty(self):
# #         return len(self.q)==0
# #     def reverse_queue(self):
# #         temp=[]
# #         while not self.is_empty():
            
# #             temp.append(self.q.pop((0)))
# #         temp.reverse()
# #         return temp
# # q=queue()
# # q.enqueue(3)
# # q.enqueue(5)
# # q.enqueue(8)
# # print(q.reverse_queue())

# # Question 3 --> Find the first non-repeating element in a queue.
# class Queue:
#     def __init__(self):
#         self.q=[]
#     def enqueue(self,val):
#         self.q.append(val)
#     def dequeue(self):
#         if not self.is_empty():
#             return self.q.pop(0)
#         return "queue is empty"
#     def check_freq(self):
#         freq={}
#         # count=1
#         for ele in self.q:
#             freq[ele]=freq.get(ele,0)+1
#         for ele in self.q:
#             if freq[ele]==1:
#                 return ele
#             else:
#                 None

# q=Queue()
# q.enqueue(2)
# q.enqueue(3)
# q.enqueue(2)
# print(q.check_freq())
            





# class queue:
#     def __init__(self):

#         self.q=[]
#     def enqueue(self,val):
#         self.q.append(val)
#     def dequeue(self):
#         if not self.is_empty():
#             return self.q.pop(0)
#         return "Queue is empty"
#     def is_empty(self):
        
#         return len(self.q)==0
#     def check_repeated(self):
#         freq={}
#         for ele in self.q:
#             freq[ele]=freq.get(ele,0)+1
#         for ele in self.q:
#             if freq[ele]==1:
#                 return ele
#         return None
# Q=queue()
# Q.enqueue(2)
# Q.enqueue(4)
# Q.enqueue(5)
# Q.enqueue(2)
# print(Q.check_repeated())

 
 

# Question 4 --> Count the total number of elements in a queue without using len()..
# class stack:
#     def __init__(self):
#         self.q=[]
#     def enque(self,val):
#         self.q.append(val)
#     def deque(self):
#         if not self.is_empty():
#            return  self.q.pop(0)
#         return "Queue is empty "
#     def is_empty(self):
#         return len(self.q)==0
#     def find_len(self):
#         temp=[]
#         count=0
#         while not  self.is_empty():
#             x=self.deque()
#             temp.append(x)
#             count+=1
#         for x in temp:
#             self.enque(x)
#         return count
# q=stack()
# q.enque(2)
# q.enque(4)
# q.enque(6)
# print(q.find_len())

    

# question 5 --> Display all elements of a queue without removing them.

# class queue:
#     def __init__(self):
#         self.q=[]
#     def enqueue(self,val):
#         self.q.append(val)
#     def dequeue(self):
#         if not self.is_empty():
#             return self.q.pop(0)
#         return "queue is empty "
#     def is_empty(self):
#         return len(self.q)==0
#     def display(self):
#         temp=[]
#         while not self.is_empty():
#             return self.q[:]
# s=queue()
# s.enqueue(2)
# s.enqueue(3)
# s.enqueue(5)
# s.enqueue(7)
# print(s.display())


# Question 6 ---> Reverse a queue using a stack.

# class queue:
#     def __init__(self):
#         self.q=[]
#     def enqueue(self,val):
#         self.q.append(val)
#     def dequeue(self):
#         if not self.is_empty():
#             return self.q.pop(0)
#         return "Queue is empty "
#     def is_empty(self):
#         return len(self.q)==0
#     def reverse_q(self):

#         temp=[]
#         while not self.is_empty():
#             temp.append(self.q.pop(0))
#         temp.reverse()
#         return temp
# q=queue()
# q.enqueue(2)
# q.enqueue(3)
# q.enqueue(5)
# print(q.reverse_q())



# Question 7 --> Given a queue of numbers, double each value and print the queue.
# class queue:
#     def __init__(self):
#         self.q=[]
#     def push(self,val):
#         self.q.append(val)
#     def pop(self):
#         if not self.is_empty():
#             return self.q.pop(0)
#         return "Queue is empty "
#     def is_empty(self):
#         return len(self.q)==0
#     def double_each(self):
#         for i in range(len(self.q)):
#             self.q[i]=self.q[i]*2
#         return self.q
# q=queue()
# q.push(3)
# q.push(4)
# q.push(6)
# q.push(7)
# print(q.double_each())


# Question 8 --> Given a queue, print only even numbers from it.
# class stack:
#     def __init__(self):
#         self.q=[]
#     def enque(self,val):
#         self.q.append(val)
#     def dequeue(self):
#         if not self.is_empty():
#             return self.q.pop(0)
#         return "Stack is empty "
#     def is_empty(self):
#         return len(self.q)==0
#     def print_even(self):
#         for i in range(len(self.q)):
#             if self.q[i]%2==0:
                
#                 print(self.q[i])
                
# q=stack()
# q.enque(3)
# q.enque(5)
# q.enque(6)
# q.enque(8)
# print(q.print_even())



# Question 9 --> Find the sum of all elements present in a queue.
# class stack:
#     def __init__(self):
#         self.q=[]
#     def enqueue(self,val):
#         self.q.append(val)
#     def dequeue(self):
#         if not self.is_empty():
#             return self.q.pop(0)
#         return "Queue is empty!"
#     def is_empty(self):
#         return len(self.q)==0
#     def sum_ele(self):
#         sum=0
#         for i in range(len(self.q)):
#             sum=sum+self.q[i]
#         return sum
# q=stack()
# q.enqueue(3)
# q.enqueue(6)

# q.enqueue(11)
# print(q.sum_ele())


# Question 11 --> Remove all negative numbers from a queue.

# class queue:
#     def __init__(self):
#         self.q=[]
#     def enqueue(self,val):
#         self.q.append(val)
#     def dequeue(self):
#         if not self.is_empty():
#             return self.q.pop(0) 
#         return "Queue is empty"
#     def is_empty(self):
#         return len(self.q)==0
#     def remove_negative(self):
#         temp=[]
#         for ele in self.q:
#             if ele>=0:
#                 temp.append(ele)
#         self.q=temp
            
#         return self.q
# q=queue()
# q.enqueue(2)
# q.enqueue(-4)
# q.enqueue(-6)
# q.enqueue(8)
# print(q.remove_negative())

# question 12 --> Check whether an element X is present in the queue or not. 
# class queue:
#     def __init__(self):
#         self.q=[]
#     def enque(self,val):
#         self.q.append(val)
#     def deque(self):
#         if not self.is_empty():
#             return self.q.pop(0)
#         return "Queue is empty"
#     def check_ele(self,val):
#         for ele in self.q:
#             if ele==val:
#                 return "True"
            
#         return "False"                                                          
# s=queue()
# s.enque(2)
# s.enque(4)
# s.enque(6)
# print(s.check_ele(6))

    

# Question 13 -->  