import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv("pet_adoption_data.csv")

# Filter for orange-colored subjects and count by pet type
orange_counts = df[df['Color'] == 'Orange']['PetType'].value_counts()

# Print exact data values for the plot
print("Orange subjects by pet type:")
for pet, count in orange_counts.items():
    print(f"- {pet}: {count}")

# Create a bar plot for orange subjects by pet type
plt.figure(figsize=(8, 5))
sns.barplot(
    x=orange_counts.index,
    y=orange_counts.values,
    palette="Oranges"
)
plt.title("Number of Orange-Colored Subjects by Pet Type")
plt.xlabel("Pet Type")
plt.ylabel("Count of Orange Subjects")
plt.tight_layout()
plt.show()