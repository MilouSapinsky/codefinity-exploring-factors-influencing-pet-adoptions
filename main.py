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
#df_cat_breeds = df_breeds[['Siamese', 'Persian']] if all(b in df_breeds for b in ['Siamese', 'Persian']) else []
df_cat_breeds = df[df['PetType'] == 'Cat']['Breed'].unique()
print(f"Cat breeds: {df_cat_breeds}")
# Add a new column that contains the breed only for cats
#df['CatBreed'] = df['Breed'].where(df['PetType'] == 'Cat', None)
cat_breed_count = df_cat_breeds.shape[0]
print(f"Cat breed count: {cat_breed_count}")
siamese = df[(df['Breed'] == 'Siamese')].shape[0]
print(f"Siamese: {siamese}")
persian = df[(df['Breed'] == 'Persian')].shape[0]
print(f"Persian: {persian}")
colors = df['Color'].unique()
print(f"Colors: {colors}")
orange_cats = df.loc[(df['PetType'] == 'Cat') & (df['Color'] == 'Orange')]
orange_cats_count = orange_cats.shape[0]
print(f"Orange cats: {orange_cats_count}")
white_cats = df.loc[(df['PetType'] == 'Cat') & (df['Color'] == 'White')]
white_cats_count = white_cats.shape[0]
print(f"White cats: {white_cats_count}")




