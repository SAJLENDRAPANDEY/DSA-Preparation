import pandas as pd
import random

# Generate dataset with 50 rows
data = {
    "CGPA": [round(random.uniform(5.0, 10.0), 2) for _ in range(50)],
    "Score": [round(random.uniform(0.0, 10.0), 2) for _ in range(50)],
    "Placed": [random.choice([0, 1]) for _ in range(50)]
}

df = pd.DataFrame(data)

# Save Excel file
file_name = "cgpa_score_points_placed_50.xlsx"
df.to_excel(file_name, index=False)
print(f"Excel file created: {file_name}")
