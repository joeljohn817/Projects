import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

observations = pd.read_csv("C:\\Users\\Joel John\\OneDrive\\Desktop\\Codecademy\\Biodiversity\\biodiversity-solution\\observations.csv")
species = pd.read_csv("C:\\Users\\Joel John\\OneDrive\\Desktop\\Codecademy\\Biodiversity\\biodiversity-solution\\species_info.csv")


# check for nan values in data 
print(species.isna().sum())
print(observations.isna().sum())
#Fill in missing values
species = species.fillna(value={'conservation_status':'Safe'})

# check for and drop duplicates  
print(species[species.duplicated(subset=['scientific_name'])])
species.drop_duplicates(subset=['scientific_name'], keep='last', inplace=True)
print(observations[observations.duplicated(subset=['scientific_name', 'park_name'])])

#total number of observations for duplicate records and then remove the duplicates
observations['total'] = observations.groupby(['scientific_name', 'park_name'])['observations'].transform('sum')
observations.drop_duplicates(subset=['scientific_name', 'park_name'], keep='last', inplace=True)
observations = observations[['scientific_name', 'park_name', 'total']]
observations = observations.rename(columns={'total': 'observations'})


# Exploring Species Data

print(f'The number of uniques species is {species.scientific_name.nunique()}')
print(f'The number of categories are  {species.category.nunique()}')
print(f'Categories: {species.category.unique()}')
print(f'The number of species per category:{species.groupby(species.category).size()}')
print(f"number of conservation statuses:{species.conservation_status.nunique()}")
print(f"unique conservation statuses:{species.conservation_status.unique()}")
print(f'The number of species per conservation status:{species.groupby("conservation_status").size()}')

# # Exploring Obseravtion Data
print(f'The number of observations per park is: {observations.observations.groupby(observations.park_name).sum().reset_index()}')
print(f"number of parks:{observations.park_name.nunique()}")
print(f"unique parks:{observations.park_name.unique()}")
print(f"number of observations:{observations.observations.sum()}")

# Combine both dataframes into one
combined_data = pd.merge(observations, species, left_on='scientific_name', right_on='scientific_name', how='left')
combined_data = combined_data[['scientific_name', 'park_name', 'observations', 'category', 'conservation_status']]

print(combined_data.head(10))
print(combined_data.category.value_counts())
print(combined_data.park_name.value_counts())
print(combined_data.conservation_status.value_counts())


# Data Analysis

# barplot categroy vs observation for each category
category_colors = {'Mammal': 'blue', 'Bird': 'green', 'Reptile': 'red', 'Amphibian': 'purple', 'Fish': 'orange', 'Vascular Plant': 'yellow', 'Nonvascular Plant': 'brown'}

fig = plt.figure(figsize=(16, 8))
sns.barplot(x='category', y='observations', data=combined_data, estimator=np.sum, hue='category', palette=category_colors)
plt.title('Number of observations by category')
plt.show()
plt.clf()

order = ['Bryce National Park', 'Great Smoky Mountains National Park', 'Yellowstone National Park', 'Yosemite National Park']

# barplot parkname vs observation for each category
fig = plt.figure(figsize=(16, 8))
sns.barplot(x='park_name', y='observations', data=combined_data, hue='category', estimator=np.sum, order=order)
plt.title('Number of observations for each categories by park')
plt.show()
plt.clf()

# barplot category vs observation for each park
fig = plt.figure(figsize=(16, 8))
sns.barplot(x='category', y='observations', data=combined_data, hue='park_name', estimator=np.sum)
plt.title('Number of observations for each park by category')
plt.show()
plt.clf()

# barplot parkname and observation for each conservation status not = safe
filtered_data = combined_data[combined_data['conservation_status'] != 'Safe']
fig = plt.figure(figsize=(16, 8))
sns.barplot(x='park_name', y='observations', data=filtered_data, hue='conservation_status', estimator=np.sum, order=order)
plt.title('Number of observations for each conservation status by park')
plt.show()
plt.clf

# Calculate category counts for observations under protection
under_protection = filtered_data['category'].value_counts().reset_index()
under_protection.columns = ['category', 'under protection']  # Rename columns directly

# Calculate total category counts
total_amount = combined_data['category'].value_counts().reset_index()
total_amount.columns = ['category', 'total']  # Rename columns directly

# Merge the two DataFrames on the 'category' column
merged_df = pd.merge(under_protection, total_amount, on='category')
merged_df['proportion %'] = round(merged_df['under protection']/merged_df['total']*100, 2)

print(merged_df)

# bar plot of number of protected species by category
fig = plt.figure(figsize=(16, 8))
sns.barplot(x='category', y='under protection', data=under_protection)
plt.xlabel('categories')
plt.ylabel('Number of protected species')
plt.title('Number of protected species by category ')
plt.show()
plt.clf()

# bar plot of proportions of protected species by category
fig = plt.figure(figsize=(16, 8))
sns.barplot(x='category', y='proportion %', data=merged_df)
plt.ylabel('proportion (%)')
plt.xlabel('categories')
plt.title('Proportions of protected species by category ')
plt.show()
plt.clf() 

# countplot Number of species by conservation status by category
fig = plt.figure(figsize=(16, 8))
sns.countplot(x='category', data=filtered_data, hue='conservation_status')
plt.legend(loc='upper right')
plt.title('Number of species by conservation status by category')
plt.show()