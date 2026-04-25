# # Print 1 to N
# def print_1(n):
#     if n==0 :
#         return 
#     print_1(n-1)
#     print(n,end=" ")
# print(print_1(5))

# q 2-->Print N to 1
def print_n_1(n):
    if n==0:
        return 
    print(n,end=" ")
    print_n_1(n-1)
    
print(print_n_1(5))