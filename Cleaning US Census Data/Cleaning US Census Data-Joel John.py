import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import glob


# Combining Multiple Files
files = glob.glob('states*.csv')

df_list = []

for filename in files:
    data = pd.read_csv(filename)
    df_list.append(data)

us_census = pd.concat(df_list)


# Data cleansing

us_census.Income = us_census.Income.replace('[\$,]','',regex=True)
us_census["Income"] = pd.to_numeric(us_census['Income'])


us_census['Men'] = us_census.GenderPop.str.split('_').str[0]
us_census.Men = us_census.Men.replace('M','',regex=True)
us_census["Men"] = pd.to_numeric(us_census['Men'])

us_census['Women'] = us_census.GenderPop.str.split('_').str[1]
us_census.Women = us_census.Women.replace('F','',regex=True)
us_census["Women"] = pd.to_numeric(us_census['Women'])


# replacing nan values in women population column
us_census['Women'] = us_census['Women'].fillna(us_census['TotalPop'] - us_census['Men'])


# remove duplicated data
us_census = us_census.drop_duplicates(subset = us_census.columns[1:])

#scatter plot of women population vs income after removing duplicates
plt.scatter(us_census.Women, us_census.Income)
plt.title('Scatter Plot of Income vs. Number of Women per State')
plt.ylabel('Income (in US Dollars')
plt.xlabel('Population of Women per State')
plt.show()
plt.clf()

# replace % symbol for each race category
us_census['Hispanic'] = us_census['Hispanic'].replace('%','', regex = True)
us_census['Hispanic']= pd.to_numeric(us_census['Hispanic'])

us_census['White'] = us_census['White'].replace('%','', regex = True)
us_census['White']= pd.to_numeric(us_census['White'])

us_census['Black'] = us_census['Black'].replace('%','', regex = True)
us_census['Black']= pd.to_numeric(us_census['Black'])

us_census['Native'] = us_census['Native'].replace('%','', regex = True)
us_census['Native']= pd.to_numeric(us_census['Native'])

us_census['Asian'] = us_census['Asian'].replace('%','', regex = True)
us_census['Asian']= pd.to_numeric(us_census['Asian'])

us_census['Pacific'] = us_census['Pacific'].replace('%','', regex = True)
us_census['Pacific']= pd.to_numeric(us_census['Pacific'])

# filling nan values with the mean value of their respected columns
us_census.fillna(value={
    'Pacific': us_census['Pacific'].mean(),
    'Hispanic': us_census['Hispanic'].mean(),
    'White': us_census['White'].mean(),
    'Black': us_census['Black'].mean(),
    'Native': us_census['Native'].mean(),
    'Asian': us_census['Asian'].mean(),
}, inplace=True)


# Plotting Histograms
fig, ax = plt.subplots(2, 3, figsize=(15, 10))  # Adjust the figure size as needed


ax[0][0].hist(us_census['Hispanic'])
ax[0][1].hist(us_census['Pacific'])
ax[0][2].hist(us_census['White'])
ax[1][0].hist(us_census['Black'])
ax[1][1].hist(us_census['Native'])
ax[1][2].hist(us_census['Asian'])

# Set titles and labels for each subplot
ax[0][0].set(title='Hispanic', xlabel='% of population', ylabel='Number of states')
ax[0][1].set(title='Pacific', xlabel='% of population', ylabel='Number of states')
ax[0][2].set(title='White', xlabel='% of population', ylabel='Number of states')
ax[1][0].set(title='Black', xlabel='% of population', ylabel='Number of states')
ax[1][1].set(title='Native', xlabel='% of population', ylabel='Number of states')
ax[1][2].set(title='Asian', xlabel='% of population', ylabel='Number of states')

# Set the title for the entire figure
fig.suptitle('Histograms for different races',fontsize=15)

plt.show()