# factorial 
# def fact(n):
#     if n==0 or n==1:
#         return 1
#     return n*fact(n-1)
# n=int(input("Enter the number:"))
# print(fact(n))

# q--> 2 Print Numbers from 1 to N
# def print_1_to_n(n):
#     for i in range(1,n+1):
#         print(i,end=' ')
# n=int(input("enter the number :"))
# print(print_1_to_n(n))

# q 3 --> Print Numbers from 1 to N
# def print_n(n):
#     if n==0:
#         return
#     print_n(n-1)
#     print(n,end=" ")
# n=int(input("Enter the number : "))
# print(print_n(n))


# q 4 --> Print Numbers from N to 1
# def print_n(n):
#     if n==0:
#         return
#     print_n(n)
#     print(n-1,end=" ")
# n=int(input("enter the number "))
# print(print_n(n))
    

# q 5 --> Sum of First N Natural Numbers
# def sum_n(n):
#     if n==1:
#         return 1
#     return n+sum_n(n-1)
# print(sum_n(5))

# q 6 --> Fibonacci Series
# def fibonacci(n):
#     if n==0:
#         return 0
#     elif n==1:
    
#         return 1
#     else:
#         return fibonacci(n-1)+fibonacci(n-2)
# n=int(input("Enter the number:"))
# for i in range(n):
#     print(fibonacci(i),end=" ")


# q 7 --> Sum of Digits of a Number
# def add_num(n):
#     if n==0:
#         return 0
#     return(n%10)+add_num(n//10)
# n=int(input("Enter digit "))
# print(add_num(n))

# q 8 --> Reverse a String
# def reverse_str(s):
#     if len(s)==0:
#         return s
#     return reverse_str(s[1:])+s[0]
# s=input("enter ")
# print(reverse_str(s))

# q 9 --> Check Palindrome String
# def chech_palin(s):
#     return s[::-1]==s
# s="mdmw"
# print(chech_palin(s))

# q 10 --> Power of a Number
# def power_n(n,po):
#     return pow(n,po)
# print(power_n(2,3))

# def pow_n(x,n):
#     if n==0:
#         return 1
#     return x*pow_n(x,n-1)
# print(pow_n(2,3))

# q 11 --> Product of Digits of a Number
# def digit(n):
#     if n<10:
#         return n
#     return (n%10)*digit(n//10)
# print(digit(1234))


# def fibonacci(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fibonacci(n-1)+fibonacci(n-2)
# n=int(input("enter :"))
# for i in range(n):
#     print(fibonacci(i),end=" ")


# pq 2 sum of digit of number
# def  sum_digit(n):
#     if n==0:
#         return 0
#     return (n%10)+sum_digit(n//10)
# n=123
# print(sum_digit(n))

# PQ 3 --> product of digit of number
# def product_num(num):
#     if num==0:
#         return 0
#     elif num==1:
#         return 1
#     else:
#         return (num%10)*product_num(num//10)
# num=1234
# print(product_num(num))


# factorial of number 
# def fact(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return n*fact(n-1)
# n=5
# print(fact(n))

