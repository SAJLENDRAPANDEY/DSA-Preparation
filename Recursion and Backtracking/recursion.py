# # Print 1 to N
# def print_1(n):
#     if n==0 :
#         return 
#     print_1(n-1)
#     print(n,end=" ")
# print(print_1(5))

# q 2-->Print N to 1
# def print_n_1(n):
#     if n==0:
#         return 
#     print(n,end=" ")
#     print_n_1(n-1)
    
# print(print_n_1(5))


# Q 3 ->Fibonacci
# def fibonacci(n):
#     if n==0 :
#         return 0
#     elif n==1:
#         return 1
    
#     return fibonacci(n-1)+fibonacci(n-2)
# print(fibonacci(5))



#  or reduce complexity
# def fibonacci(n,dp={}):
#     if n in dp:
#         return dp[n]
#     if n==0:
#         return 0
#     if n==1:
#         return 1
#     dp[n]=fibonacci(n-1,dp)+fibonacci(n-2,dp)

#     return dp[n]
# print(fibonacci(5))


# Q 4 --> Sum of N numbers
# def sum_n(n):
#     if n==0:
#         return 0
#     if n==1:
#         return 1
#     return n+sum_n(n-1)
# print(sum_n(5))



# Q 5 --> 
# def factorial(n):
#     # Base case
#     if n == 0 or n == 1:
#         return 1
    
#     # Recursive case
#     return n * factorial(n - 1)

# # Example usage
# print(factorial(5))  # Output: 120



# Q 6 ->
# def fibonacci(n):
#     # Base case
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
    
#     # Recursive case
#     return fibonacci(n-1) + fibonacci(n-2)

# # Example usage
# print(fibonacci(6))  # Output: 8



# Q 7->Sum of N numbers
# def sum_n(n):
#     if n==0:
#         return 0
#     if n==1:
#         return 1
#     return n+sum_n(n-1)
# print(sum_n(5))


# Q 8 --> 
# def printNos(n):
#         #Code here
#         if n==0:
#             return 0
#         printNos(n-1)
#         print(n,end=" ")
        
# print(printNos(5))


# Q 9>Sum of first N numbers
# def sum_n(n):
#     sum=0
#     i=1
#     while i<=n:
#         sum=sum+i
#         i=i+1
#     return sum
# print(sum_n(5))


# 10 -- Fibonacci
# def nthFibonacci(n: int) -> int:
#         # code here
#         if n==0:
#             return 0
#         if n==1:
#             return 1
#         return nthFibonacci(n-2)+nthFibonacci(n-1)

# print(nthFibonacci(5))


# 11-> Palindrome number
# def palindrome(n):
#     n=str(n)
#     left=0
#     right=len(n)-1
#     while left<=right:
#         if n[left]!=n[right]:
#             return False
#         left+=1
#         right-=1
#     return True
# print(palindrome(3555))



# Q 12 -.> count digit of a number
def count_digit(n):
    count=0
    while n >0:
        count+=1
        n=n//10
    return count
print(count_digit(2323))