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

# Extend y-axis to include values over 100
max_count = orange_counts.max()
plt.ylim(0, max(100, max_count) + 10)  # ensures the top is at least 110 or higher if needed

plt.tight_layout()
plt.show()

large_counts = df[df['Size'] == 'Large']['PetType'].value_counts()
plt.figure(figsize=(8,5))
sns.barplot(
    x=large_counts.index,
    y=large_counts.values,
    palette="cool"
)
plt.title("Number of Large-sized subjects by Pet type")
plt.xlabel("Pet Type")
plt.ylabel("Count of large subjects")
plt.tight_layout()
plt.show()




