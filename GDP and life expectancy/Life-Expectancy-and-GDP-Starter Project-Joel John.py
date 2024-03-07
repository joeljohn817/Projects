import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Load Data
df = pd.read_csv("C:\\Users\\Joel John\\OneDrive\\Desktop\\Codecademy\\Life-Expectancy-and-GDP-Starter\\Life-Expectancy-and-GDP-Starter\\all_data.csv")
print(df.head())

# rename column
df.rename(columns={'Life expectancy at birth (years)' : 'life_expect'}, inplace=True)
df["gdp_billion"] = df.GDP/1000000000

# defining variables for year, life expectancy and gdp
chile_year = df.Year[df.Country == 'Chile']
chile_life_expect = df.life_expect[df.Country == 'Chile']
chile_gdp = df.gdp_billion[df.Country == 'Chile']

china_year = df.Year[df.Country == 'China']
china_life_expect = df.life_expect[df.Country == 'China']
china_gdp = df.gdp_billion[df.Country == 'China']

germany_year = df.Year[df.Country == 'Germany']
germany_life_expect = df.life_expect[df.Country == 'Germany']
germany_gdp = df.gdp_billion[df.Country == 'Germany']

mexico_year = df.Year[df.Country == 'Mexico']
mexico_life_expect = df.life_expect[df.Country == 'Mexico']
mexico_gdp = df.gdp_billion[df.Country == 'Mexico']

usa_year = df.Year[df.Country == 'United States of America']
usa_life_expect = df.life_expect[df.Country == 'United States of America']
usa_gdp = df.gdp_billion[df.Country == 'United States of America']

zimbabwe_year = df.Year[df.Country == 'Zimbabwe']
zimbabwe_life_expect = df.life_expect[df.Country == 'Zimbabwe']
zimbabwe_gdp = df.gdp_billion[df.Country == 'Zimbabwe']

# Set the style
sns.set_style("darkgrid")

# Scatter Plot for GPD vs Life Expectancy for all countries
fig,ax = plt.subplots(2,3, figsize = [25,10])

ax[0,0].scatter(data = df[df.Country == 'Chile'], x = 'life_expect', y = 'gdp_billion', color = 'blue')
ax[0,0].set_title('Chile', fontsize=20)

ax[0,1].scatter(data = df[df.Country == 'China'], x = 'life_expect', y = 'gdp_billion', color = 'green')
ax[0,1].set_title('China', fontsize=20)

ax[0,2].scatter(data = df[df.Country == 'Germany'], x = 'life_expect', y = 'gdp_billion', color = 'purple')
ax[0,2].set_title('Germany', fontsize=20)

ax[1,0].scatter(data = df[df.Country == 'Mexico'], x = 'life_expect', y = 'gdp_billion', color = 'orange')
ax[1,0].set_title('Mexico', fontsize=20)

ax[1,1].scatter(data = df[df.Country == 'United States of America'], x = 'life_expect', y = 'gdp_billion', color = 'turquoise')
ax[1,1].set_title('United States of America', fontsize=20)

ax[1,2].scatter(data = df[df.Country == 'Zimbabwe'], x = 'life_expect', y = 'gdp_billion', color = 'brown')
ax[1,2].set_title('Zimbabwe', fontsize=20)

fig.suptitle('GDP vs Life Expectancy',fontsize = 20)
fig.supxlabel('Life Expectancy at Birth (Years)', fontsize = 20)
fig.supylabel('GDP (Billion $)', fontsize = 20)
fig.legend(['Chile', 'China', 'Germany', 'Mexico', 'United States of America', 'Zimbabwe'], loc ='center right')

plt.savefig('Life_Expectancy_GDP_Per_Country')
plt.show()
plt.clf()


# lineplot of the change in life expectancy for each country throughtout the years

fig,ax = plt.subplots(2,3, figsize = [25,10])

ax[0,0].plot(chile_year,chile_life_expect, color = 'blue',linestyle = '--', marker = 'o')
ax[0,0].set_title('Chile', fontsize=20)

ax[0,1].plot(china_year,china_life_expect, color = 'green',linestyle = '--', marker = 'o')
ax[0,1].set_title('China', fontsize=20)

ax[0,2].plot(germany_year,germany_life_expect, color = 'purple',linestyle = '--', marker = 'o')
ax[0,2].set_title('Germany', fontsize=20)

ax[1,0].plot(mexico_year,mexico_life_expect, color = 'orange',linestyle = '--', marker = 'o')
ax[1,0].set_title('Mexico', fontsize=20)

ax[1,1].plot(usa_year,usa_life_expect, color = 'turquoise',linestyle = '--', marker = 'o')
ax[1,1].set_title('United States of America', fontsize=20)

ax[1,2].plot(zimbabwe_year,zimbabwe_life_expect, color = 'brown',linestyle = '--', marker = 'o')
ax[1,2].set_title('Zimbabwe', fontsize=20)

fig.suptitle('Life Expectancy Over the Years',fontsize = 20)
fig.supylabel('Life Expectancy at Birth (Years)', fontsize = 20)
fig.supxlabel('Years', fontsize = 20)
fig.legend(['Chile', 'China', 'Germany', 'Mexico', 'United States of America', 'Zimbabwe'], loc ='center right')

plt.savefig('Life_Expectancy_Per_Country')
plt.show()
plt.clf()

# Life Expectancy line charts complied into one figure
plt.figure(figsize=[25,10])

plt.plot(chile_year,chile_life_expect, color = 'blue',linestyle = '--', marker = 'o')
plt.plot(china_year,china_life_expect, color = 'green',linestyle = '--', marker = 'o')
plt.plot(germany_year,germany_life_expect, color = 'purple',linestyle = '--', marker = 'o')
plt.plot(mexico_year,mexico_life_expect, color = 'orange',linestyle = '--', marker = 'o')
plt.plot(usa_year,usa_life_expect, color = 'turquoise',linestyle = '--', marker = 'o')
plt.plot(zimbabwe_year,zimbabwe_life_expect, color = 'brown',linestyle = '--', marker = 'o')

plt.title('Life Expectancy Over the Years',fontsize = 20)
plt.ylabel('Life Expectancy at Birth (Years)', fontsize = 20)
plt.xlabel('Years', fontsize = 20)
plt.legend(['Chile', 'China', 'Germany', 'Mexico', 'United States of America', 'Zimbabwe'], loc ='center left')

plt.savefig('Combined_Life_Expectancy.png')
plt.show()


# lineplot of the change in GDP for each country throughtout the years

fig,ax = plt.subplots(2,3, figsize = [25,10])

ax[0,0].plot(chile_year,chile_gdp, color = 'blue',linestyle = '--', marker = 'o')
ax[0,0].set_title('Chile', fontsize=20)

ax[0,1].plot(china_year,china_gdp, color = 'green',linestyle = '--', marker = 'o')
ax[0,1].set_title('China', fontsize=20)

ax[0,2].plot(germany_year,germany_gdp, color = 'purple',linestyle = '--', marker = 'o')
ax[0,2].set_title('Germany', fontsize=20)

ax[1,0].plot(mexico_year,mexico_gdp, color = 'orange',linestyle = '--', marker = 'o')
ax[1,0].set_title('Mexico', fontsize=20)

ax[1,1].plot(usa_year,usa_gdp, color = 'turquoise',linestyle = '--', marker = 'o')
ax[1,1].set_title('United States of America', fontsize=20)

ax[1,2].plot(zimbabwe_year,zimbabwe_gdp, color = 'brown',linestyle = '--', marker = 'o')
ax[1,2].set_title('Zimbabwe', fontsize=20)

fig.suptitle('GDP Over the Years',fontsize = 20)
fig.supylabel('GDP (Billion $)', fontsize = 20)
fig.supxlabel('Years', fontsize = 20)
fig.legend(['Chile', 'China', 'Germany', 'Mexico', 'United States of America', 'Zimbabwe'], loc ='center right')

plt.savefig('GDP_Per_Country.png')
plt.show()
plt.clf()

# GDP line charts complied into one figure
plt.figure(figsize=[25,10])

plt.plot(chile_year,chile_gdp, color = 'blue',linestyle = '--', marker = 'o')
plt.plot(china_year,china_gdp, color = 'green',linestyle = '--', marker = 'o')
plt.plot(germany_year,germany_gdp, color = 'purple',linestyle = '--', marker = 'o')
plt.plot(mexico_year,mexico_gdp, color = 'orange',linestyle = '--', marker = 'o')
plt.plot(usa_year,usa_gdp, color = 'turquoise',linestyle = '--', marker = 'o')
plt.plot(zimbabwe_year,zimbabwe_gdp, color = 'brown',linestyle = '--', marker = 'o')

plt.title('GDP Over The Years',fontsize = 20)
plt.ylabel('GDP (Billion $)', fontsize = 20)
plt.xlabel('Years', fontsize = 20)
plt.legend(['Chile', 'China', 'Germany', 'Mexico', 'United States of America', 'Zimbabwe'], loc ='upper left')

plt.savefig('Combined_GDP.png')
plt.show()
plt.clf()

# Calculate average life expectancy for each country
average_life_expectancy = df.groupby('Country')['life_expect'].mean()

# Print average life expectancy for each country
print("Average Life Expectancy in Each Country:")
print(average_life_expectancy)

# Create a histogram of life expectancy
plt.figure(figsize=(10, 6))

sns.histplot(data=df, x='life_expect', bins=30, kde=True)
plt.title('Distribution of Life Expectancy')
plt.xlabel('Life Expectancy at Birth (Years)')
plt.ylabel('Frequency')

plt.savefig('life_Expectancy_histogram.png')
plt.show()

