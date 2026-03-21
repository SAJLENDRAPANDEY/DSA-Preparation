# # # import pandas as pd
# # # import numpy as np
# # # data={'First Score': [100, 90, np.nan, 95],
# # #         'Second Score': [30, 45, 56, np.nan],
# # #         'Third Score': [np.nan, 40, 80, 98]}
# # # df=pd.DataFrame(data)
# # # print(df)

# # # # is null()
# # # # print(df.isnull().sum())

# # # # print(df.isnull())

# # # # fill na
# # # print(df['First Score'].mean())

# # # print(df.fillna(95))


# # #  1 -->
# # import pandas as pd
# # import numpy as np

# # data=pd.read_csv(r"C:\yash_important data\Employee data 2.csv")
# # print(data)


# # print(data.isnull().sum())



# # 2 --> Using isna()
# # import pandas as pd
# # import numpy as np
# # d = {'First Score': [100, 90, np.nan, 95],
# #         'Second Score': [30, 45, 56, np.nan],
# #         'Third Score': [np.nan, 40, 80, 98]}
# # df=pd.DataFrame(d)
# # print(df)

# # print(df.notnull())

# # print(df.isna())


# # import pandas as pd
# # data=pd.read_csv(r"C:\yash_important data\Employee data 2.csv")
# # print(data)

# # nmg=pd.notnull(data["jobcat"])
# # x=data[nmg]
# # print(x)



# #  2 --> fill na 
# import pandas as pd
# import numpy as np
# d = {'First Score': [100, 90, np.nan, 95],
#         'Second Score': [30, 45, 56, np.nan],
#         'Third Score': [np.nan, 40, 80, 98]}
# df = pd.DataFrame(d)
# print(df)

# print(df.isnull().sum())

# print(df.fillna(method='pad'))

# print(df.fillna(method='bfill'))



# interpolate --> works at linear 
import pandas as pd
df = pd.DataFrame({"A": [12, 4, 5, None, 1], 
                   "B": [None, 2, 54, 3, None], 
                   "C": [20, 16, None, 3, 8], 
                   "D": [14, 3, None, None, 6]})  

print(df)

print(df.interpolate(method='linear',limit_direction='forward'))

