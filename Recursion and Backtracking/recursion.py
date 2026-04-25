# Print 1 to N
def print_1(n):
    if n==0 :
        return 
    print_1(n-1)
    print(n,end=" ")
print(print_1(5))