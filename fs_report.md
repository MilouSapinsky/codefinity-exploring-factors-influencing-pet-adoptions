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
df_cats = df.loc[df['PetType'] == 'Cat'].shape[0]
print(f"Cats: {df_cats}")
df_breeds = df['Breed'].unique()
print(f"Breeds: {df_breeds}")
#df_cat_breeds = df_breeds[['Siamese', 'Persian']] if all(b in df_breeds for b in ['Siamese', 'Persian']) else []
df_cat_breeds = df[df['PetType'] == 'Cat']['Breed'].unique()
print(f"Cat breeds: {df_cat_breeds}")
# Add a new column that contains the breed only for cats
#df['CatBreed'] = df['Breed'].where(df['PetType'] == 'Cat', None)
cat_breed_count = df_cat_breeds.shape[0]
print(f"Cat breed count: {cat_breed_count}")
siamese = df[(df['PetType'] == 'Siamese')].shape[0]
print(f"Siamese: {siamese}")




````
