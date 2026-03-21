s="hello"
x={'a','e','i','o','u','A','E','I','O','U'}

count=0
for char in (s):
    if char in x:
        
        count+=1
print(count)