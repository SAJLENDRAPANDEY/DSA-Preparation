import pandas as pd
import numpy as np
data=np.array([3, 4, 5, 6, 12, 13, 14, 15])

n=len(data)

q1=(n+1)//4
q2=(n+1)//2
q3=(3*(n+1))//4

print(data[q1])
print(data[q2])
print(data[q3])


