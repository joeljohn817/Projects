import pandas as pd
import numpy as np
from scipy.stats import pearsonr, chi2_contingency
import matplotlib.pyplot as plt
import seaborn as sns


np.set_printoptions(suppress=True, precision = 2)

nba = pd.read_csv('./nba_games.csv')

# Subset Data to 2010 Season, 2014 Season
nba_2010 = nba[nba.year_id == 2010]
nba_2014 = nba[nba.year_id == 2014]

print(nba_2010.head())
print(nba_2014.head())

# 2010 NBA DATA
# Create series for 2 team using points column from nba_10 data frame
knicks_pts_10 = nba_2010.pts[nba.fran_id == 'Knicks']
nets_pts_10 = nba_2010.pts[nba.fran_id == 'Nets']

# calculate and print the difference in mean scores
knicks_mean_score = np.mean(knicks_pts_10)
nets_mean_score = np.mean(nets_pts_10)
diff_means_2010 = knicks_mean_score - nets_mean_score
print(diff_means_2010)

# create an overlapping histogram 
plt.hist(knicks_pts_10, color='blue', label='Knicks 2010 pts', density=1,alpha = 0.5)
plt.hist(nets_pts_10, color='blue', label='Nets 2010 pts', density=1, alpha = 0.5)
plt.legend()
plt.show()
plt.clf()


# NBA 2014 DATA
# Create series for 2 team using points column from nba_14 data frame
knicks_pts_14 = nba_2014.pts[nba.fran_id == 'Knicks']
nets_pts_14 = nba_2014.pts[nba.fran_id == 'Nets']

# calculate and print the difference in mean scores
knicks_mean_score = np.mean(knicks_pts_14)
nets_mean_score = np.mean(nets_pts_14)
diff_means_2014 = knicks_mean_score - nets_mean_score
print(diff_means_2010)

# create an overlapping histogram 
plt.hist(knicks_pts_14, color='blue', label='Knicks 2014 pts', density=1,alpha = 0.5)
plt.hist(nets_pts_14, color='blue', label='Nets 2014 pts', density=1, alpha = 0.5)
plt.legend()
plt.show()
plt.clf()


# side by side boxplot of 2010 data
sns.boxplot(data = nba_2010, x = 'fran_id', y = 'pts')
plt.show()
plt.clf()


# contingency table of frequencies that show the counts of game_result and game_location
location_result_freq = pd.crosstab(nba_2010.game_result, nba_2010.game_location)
print(location_result_freq)

#convert table of frequncies to table of proportions
location_result_proportions = location_result_freq / len(nba_2010)
print(location_result_proportions)

# calculate the expected contingency table (if there were no association) and the Chi-Square statistic
chi2, pval, dof, expected = chi2_contingency(location_result_freq)
print(expected)
print(chi2)

# calculate the covariance between forecast (538’s projected win probability) and 
# point_diff (the margin of victory/defeat) in the dataset
point_diff_forecast_cov = np.cov(nba_2010.point_diff, nba_2010.forecast)
print(point_diff_forecast_cov)

# Calculate the correlation between forecase and point_diff
point_diff_forecast_corr = pearsonr(nba_2010.forecast, nba_2010.point_diff)
print(point_diff_forecast_corr)

#scatter plot of forecast and point_diff
plt.scatter(x = nba_2010.forecast, y = nba_2010.point_diff)
plt.xlabel('Forecasted Win Prob.')
plt.ylabel('Point Differential')
plt.show()