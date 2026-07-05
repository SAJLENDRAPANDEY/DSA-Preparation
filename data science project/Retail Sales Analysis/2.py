import pandas as pd

# try robust reading
df = pd.read_csv(
    "C:/Users/SAJLE/Downloads/final_clean12.csv",
    encoding='latin1',          # 🔥 change encoding
    engine='python',            # 🔥 important
    quoting=3,                  # 🔥 ignore quotes
    on_bad_lines='skip'         # skip broken rows
)

# save cleaned file
df.to_csv("C:/Users/SAJLE/Downloads/final_clean_strong.csv", index=False)

print(len(df))