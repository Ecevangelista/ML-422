#EDA for Ames Housing Data

import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import statistics
import numpy as np
from statsmodels.graphics.gofplots import qqplot
from scipy.stats import norm,uniform
from sklearn import preprocessing

pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 81)
pd.set_option

df_train = pd.read_csv(r'C:\Users\Elaine\Desktop\Python 422\Mod1\housing_train.csv')
df_train.head()

# Get summary statistics of all variables
df_train.describe(include = 'all')

# Boxplot SalePrice to review outliers
sns.set_style("whitegrid")
sns.boxplot(x = df_train['SalePrice'])
plt.title('Distribution SalePrice')
plt.savefig('box_distribution_SalePrice.png')
plt.show()

# Histogram SalePrice to review distribution
plt.hist(df_train['SalePrice'],bins = 'auto' )
plt.title('SalePrice Histogram')
plt.savefig('assign1_histogram_SalePrice_autobin')
plt.show

# Q-Q Plot to look at normality of SalePrice
qqplot(df_train['SalePrice'],norm, fit = True, line = "45")
plt.title("Q-Q Plot SalePrice")
plt.savefig('qqplot saleprice.png')
plt.show()

# Identifying Columns with NA
nan_cols = [i for i in df_train.columns if df_train[i].isnull().any()]
print(nan_cols)
print("Total NA Columns", len(nan_cols))

# Reviewed summary statistics of Outliers and Extreme outliers to learn SaleCondition for these homes

# Outliers in SalePrice
salepriceoutlier = df_train[df_train['SalePrice'] >=341037.50]
salepriceoutlier.describe(include = 'all')

# Extreme Outliers in SalePrice
extsaleprice = df_train[df_train['SalePrice'] >= 467675.00]
extsaleprice.describe(include = 'all')

# Investigating predictors of SalePrice

# Produce correlation for continuous variables with SalePrice to assess variables with highest correlation
columns = [ 'SalePrice', 'LotFrontage', 'LotArea', 'OverallQual', 'OverallCond', 'YearBuilt', 'TotalBsmtSF', 'FullBath',
            'GrLivArea','BedroomAbvGr', 'TotRmsAbvGrd', 'Fireplaces','GarageArea' ]
df_train_corr = df_train[columns]
df_train_corr.corr()

corrmat = df_train_corr.corr()

f, ax = plt.subplots(figsize = (9,6))

sns.heatmap(corrmat, vmin = -1, vmax = 1, square=True, annot = True, cmap = 'RdYlBu', linewidths =.5)
plt.title('Correlation SalePrice')
plt.savefig('corr_saleprice_contvar.png')
plt.show()

# Top 3 Predictors: OverallQual, GrLivArea, GarageArea
# Created scatterplots to assess relationship with SalePrice

# OverallQual & SalePrice
plt.scatter(df_train['OverallQual'], df_train['SalePrice'])
plt.xlabel("OverallQual")
plt.ylabel('SalePrice')
plt.title('OverallQual vs. SalePrice')
plt.savefig('scatter overall_qual saleprice.png')
plt.show()

# GrlivArea vs. SalePrice
plt.scatter(df_train['GrLivArea'], df_train['SalePrice'])
plt.xlabel("Above Ground Living Area (SqFt)")
plt.ylabel('SalePrice')
plt.title('Above Ground Living Area vs. SalePrice')
plt.savefig('scatter grlivearea saleprice.png')
plt.show()

#GarageArea vs. SalePrice
plt.scatter(df_train['GarageArea'], df_train['SalePrice'])
plt.xlabel("Garage Area (SqFt)")
plt.ylabel('SalePrice')
plt.title('Garage Area vs. SalePrice')
plt.savefig('scatter garage_area saleprice.png')
plt.show()

# Explore outliers on OverallQual and SalePrice to learn SaleCondition
# Exploring Outlier AbvGrdLiving Area
abvlivoutl = df_train[df_train['GrLivArea']>=4000]

# Exploring Outliers Garage Area
garareaoutl = df_train[df_train['GarageArea']>=1200]

# Create new predictor TotalSqftCalc
df_train['TotalSqftCalc'] = df_train.apply(lambda row:row.TotalBsmtSF + row.GrLivArea, axis =1)
print(df_train)

# Correlation between TotalSqftCalc and SalePrice
corr_TotalSqftCalc = df_train['TotalSqftCalc'].corr(df_train['SalePrice'])
print("TotalSqftCalc and SalePrice Correlation", corr_TotalSqftCalc)

# Transform SalePrice with MinMax scaling
min_max_scaler = preprocessing.MinMaxScaler()
df_train_SalePrice_minmax = min_max_scaler.fit_transform(df_train[['SalePrice']])
print("Minmax scaler max", np.max(df_train_SalePrice_minmax))
print("Minmax scaler min", np.min(df_train_SalePrice_minmax))

# Transform SalePrice with Standard Scaler
# Print minimum and maximum values produced by Standard Scaler to learn difference in range from MinMax Scaling
standard_scaler = preprocessing.StandardScaler()
df_train_SalePrice_standard = standard_scaler.fit_transform(df_train[['SalePrice']])
print("Standard scaler max", np.max(df_train_SalePrice_standard))
print("Standard scaler min", np.min(df_train_SalePrice_standard))

