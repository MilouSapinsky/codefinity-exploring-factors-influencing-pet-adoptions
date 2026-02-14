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
#print(df.head())

# Your code starts here
df_count = df['PetID'].shape[0]
print(f"Number of subjects: {df_count}")
df_type = df['PetType'].unique()
print(f"Pet types: {df_type}")
df_cats = df[df['PetType'] == 'Cat'].shape[0]
print(f"Cats: {df_cats}")
df_breeds = df['Breed'].unique()
print(f"Breeds: {df_breeds}")
df_cat_breeds = df[df['PetType'] == 'Cat']['Breed'].unique()
print(f"Cat breeds: {df_cat_breeds}")
cat_breed_count = df_cat_breeds.shape[0]
print(f"Cat breed count: {cat_breed_count}")
siamese = df[df['Breed'] == 'Siamese'].shape[0]
print(f"Siamese: {siamese}")
persian = df[df['Breed'] == 'Persian'].shape[0]
print(f"Persian: {persian}")
colors = df['Color'].unique()
print(f"Colors: {colors}")

orange_cats = df.loc[(df['PetType'] == 'Cat') & (df['Color'] == 'Orange')]
orange_cats_count = orange_cats.shape[0]
print(f"Orange cats: {orange_cats_count}")

white_cats = df.loc[(df['PetType'] == 'Cat') & (df['Color'] == 'White')]
white_cats_count = white_cats.shape[0]
print(f"White cats: {white_cats_count}")

gray_cats = df.loc[(df['PetType'] == 'Cat') & (df['Color'] == 'Gray')]
gray_cats_count = gray_cats.shape[0]
print(f"Gray cats: {gray_cats_count}")

# Loop to count cats by each color
print("Number of cats by color:")
for color in df['Color'].unique():
    count = df[(df['PetType'] == 'Cat') & (df['Color'] == color)].shape[0]
    print(f"{color}: {count}")

# Loop to count number of subjects of every color for each pet type
print("Number of subjects by pet type and color:")
for pet in df['PetType'].unique():
    for color in df['Color'].unique():
        count = df[(df['PetType'] == pet) & (df['Color'] == color)].shape[0]
        print(f"{pet} - {color}: {count}")

# loop to count number of subjects of every size for each type
print("Number of subjects by pet type and size:")
for pet in df['PetType'].unique():
    for size in df['Size'].unique():
        count = df[(df['PetType'] == pet) & (df['Size'] == size)].shape[0]
        print(f"{pet} - {size} : {count}")








````
