# import pandas as pd
# data=pd.DataFrame([[2,4,9,6],
#                    [6,3,1,8],
#                    [7,2,1,9]],
#                    columns=['math','history','physics','bio'])
# print(data)

# # 1--> sum of all values
# # print(data.sum())

# # 2 -->aggregation
# # print(data.agg(['sum','max','min']))

# # 3 --> group
import pandas as pd
data = {
    'Item': ['Cake', 'Cake', 'Bread', 'Pastry', 'Cake'],
    'Flavor': ['Chocolate', 'Vanilla', 'Whole Wheat', 'Strawberry', 'Chocolate'],
    'Price': [250, 220, 80, 120, 250]
}

df = pd.DataFrame(data)
print(df)

# base of one column 
# res=df.groupby('Item')['Price'].sum()
# print(res)


# multiple column
# group=df.groupby(["Item","Flavour"])["Price"].sum()
# print(group)

# 