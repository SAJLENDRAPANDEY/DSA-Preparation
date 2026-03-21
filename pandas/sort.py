import pandas as pd
data = {
    'Item': ['Cake', 'Cake', 'Bread', 'Pastry', 'Cake'],
    'Flavor': ['Chocolate', 'Vanilla', 'Whole Wheat', 'Strawberry', 'Chocolate'],
    'Price': [250, 220, 80, None, 250]
}

df = pd.DataFrame(data)
# print(df)


# x=df.sort_values(by='Price')
# print(x)



# x=df.sort_values(by='Price',ascending=False)
# print(x)


# multiple column

# x=df.sort_values(by=['Price','Item'])
# print(x)

# with nan
# print(df)

# sort_vsl=df.sort_values(by=['Price'],na_position='first')
# print(sort_vsl)


# 3 Choosing a Sorting Algorithm

# a --> "quick sort"
# val=df.sort_values(by=['Price'],kind='quicksort')
# print(val)
