# class Solution:
#     def findSum(self, n):
#         # code here
#         if n==0:
#             return(0)
#         elif n==1:
#             return (1)
        
#         return(n+self.findSum(n-1))
# s=Solution()
# print(s.findSum(5))

# class so:
#     def fibo(self,n):
#         if n==0 or n==1:
#             return 1
#         return self.fibo(n-1)+self.fibo(n-2)
# for i in range(n):
#     print(self.fibo(i),end=" ")
# s=so()
# print(s.fibo(4))
        

# min max element in array
# class Solution:
#     def getMinMax(self, arr):
#         # code here
#         min_ele=arr[0]
#         max_ele=arr[0]
#         for i in range(1,len(arr)):
            
#             if arr[i]>min_ele:
#                 min_ele=arr[i]
      
#             if arr[i]<max_ele:
#                 max_ele=arr[i]
#         return max_ele, min_ele
# arr=[2,3,-4,-5,8,9]
# s=Solution()
# print(s.getMinMax(arr))


# Question 1 --> Print 1 to N
# class solution:
#     def print_1(self,n):
#         for i in range(1,n+1):
#             print(i,end=" ")
            
# s=solution()
# print(s.print_1(n=5))

# using recursion
# def print_1(n):
#     if n==0:
#         return
#     print_1(n-1)
#     print(n)
# print_1(5)


# Question 2 --> Print N to 1
# def print_n_1(n):
#     for i in range(n-1,-1,-1):
#         print(i)
# print(print_n_1(5))


# Using recursion
# def print_1_n(n):
#     if n==0:
#         return
#     print(n)
#     print_1_n(n-1)
# print_1_n(5)


# Question 3 --> Sum of first N numbers
# def sum_n(n):

#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     return n+sum_n(n-1)
# print(sum_n(5))

# Question 4 -- > Factorial of N 
# def  fact_n(n):
#     if n==0 or n==1:
#         return 1
#     return n*fact_n(n-1)
# print(fact_n(5))


# question 5 --> Count digits of a number
# def count_d(n):

#     if n==0:
#         return 0
    
#     return 1+count_d(n//10)
# print(count_d(123458))



    #   withought recursion
# def count(n):
#     count=0
#     while n >0:
#         n//=10
#         count+=1
#     return count
# print(count(1234578))


# Question 6 --> Find power (x^n)
# def power_n(x,n):
#     if n==0:
#         return 1
#     return x*power_n(x,n-1)
# print(power_n(2,3))
    


# Question 7 --> Reverse a string using recursion
# def reverse_str(x):
#     if len(x)==0:
#         return "empty"
#     elif len(x)==1:
#         return x
#     return x[::-1]
# print(reverse_str("hello"))


# recursion 
# def reverse_s(s):
#     if s=="":
#         return ""
#     return reverse_s(s[1:])+s[0]
# print(reverse_s("stu"))


# Question 8 --> Check palindrome using recursion
# def palindrom(s):
#     if len(s)==0 or len(s)==1:
#         return "False"
#     return s==s[::-1]
# print(palindrom("mdm"))


# using recursion
# def palindrome(s):
#     if len(s)>1:
#         return "True"
#     elif s[0]!=s[1]:
#         return "False"
#     return palindrome(s[1:-1])
# print(palindrome("mdm"))


# questiin 9 --> Print all permutations of a string
# def permutation(s,ans):
#     if s=="":
#         print(ans)
#         return
#     for i in range(len(s)):
#         ch=s[i]
#         left=s[:i]
#         right=s[i+1:]
#         remain=left+right
#         permutation(remain,ans+ch)
# print(permutation("abs",""))


# Question 10 --> Generate all binary strings of length N
# def generate_bin(n,curr):
#     if len(curr)==n:
#         print(curr)
#         return
#     generate_bin(n,curr+"0")
#     generate_bin(n,curr+"1")

# generate_bin(3,"")


# Question 11 -- >  Combination Sum (easy version)
def comb_sum(arr,target):
    if len(arr)>2:
        return arr
    for i in range(len(arr)):
        if arr[i]+arr[i+1]==target:
            i+=1
        return arr[i],arr[i+1]
arr=[2,3,4]
target=6
print(comb_sum(arr,target))
        