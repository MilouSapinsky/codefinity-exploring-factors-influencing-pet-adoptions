This file is a merged representation of the entire codebase, combined into a single document

## Purpose
This file contains a packed representation of the entire repository's contents.
It is designed to be easily consumable by AI systems for analysis, code review,
or other automated processes.

## File Format
The content is organized as follows:
1. This summary section
2. Repository information
3. Directory structure
4. Multiple file entries, each consisting of:
  a. A header with the file path (## File: path/to/file)
  b. The full contents of the file in a code block or first three lines for files with .csv extensions

## Usage Guidelines
- This file should be treated as read-only. Any changes should be made to the
  original repository files, not this packed version.
- When processing this file, use the file path to distinguish
  between different files in the repository.
- Be aware that this file may contain sensitive information. Handle it with
  the same level of security as you would the original repository.

## Notes
- This file includes only .ipynb and .csv file contents in full or partial form
- All other file types are represented only through the directory structure
- Binary files are not included in this packed representation. Please refer to the Repository Structure section for a complete list of file paths, including binary files

# Directory Structure

````
./
fs_report.md
main.py
pet_adoption_data.csv
````

# Files

## File: pet_adoption_data.csv
````
PetID,PetType,Breed,AgeMonths,Color,Size,WeightKg,Vaccinated,HealthCondition,TimeInShelterDays,AdoptionFee,PreviousOwner,AdoptionLikelihood
500,Bird,Parakeet,131,Orange,Large,5.039767822529515,1,0,27,140,0,0
501,Rabbit,Rabbit,73,White,Large,16.086726854616735,0,0,8,235,0,0
````

## File: main.py
````
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
plt.show()````
