# generator me return ki jagah yeild ka use krte h ye one by one line return krta h memory save krta h 
# q 1 --> Even Numbers Generator
def even_number(n):
    for i in range(2,n+1,2):
        yield i 
for i in even_number(10):
    print(i)


    # generator saves the memory 
    