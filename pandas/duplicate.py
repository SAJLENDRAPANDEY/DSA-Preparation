import pandas as pd
data = {
    "Name": ["Amit", "Ravi", "Amit", "Neha", "Ravi"],
    "Age": [25, 30, 25, 22, 30]
}
df=pd.DataFrame(data)
print(df)

# print(df[df.duplicated()].count())

print(df.duplicated(keep='first'))

print(df.duplicated(keep='last'))