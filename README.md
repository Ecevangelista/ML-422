# Exploratory Data Analysis: Ames Housing Data

Exploratory Data Analysis (EDA) was performed on the Ames Housing train data set to explore and prepare data to predict housing prices for residential homes in Ames, Iowa.
EDA includes:
* Descriptive statistics and visualizations to help understand the marginal distribution of the dependent variable SalePrice
* Investigation of missing data and outliers
* Investigation of potential predictors of SalePrice
* Feature creation to generate a new predictor
* Min-max and standard scaling on dependent variable SalePrice

#### Distribution of SalePrice  
Count: 1460 observations  
Mean: $180,921.20  
Std: $79,422.50  
Min: $34,900.00  
25%: $129,975.00  
50%: $163,000.00  
75%: $214,400.00  
Max: $755,000.00  

The boxplot below shows that there are several outliers on the upper end of the SalePrice distribution.  

![box_distribution_SalePrice](https://user-images.githubusercontent.com/49419673/148699771-8511519f-4cbb-42fc-b3d5-fb578d116240.png)

The histogram shows that the distribution of SalePrice is right-skewed which indicates that the upper values would pull the mean higher.  
The Q-Q Plot helps assess and provide further confirmation of the normality of SalePrice distribution. The plot below shows that SalePrice skews upward in the back half and that SalePrice is not normally distributed. The skewed distribution of SalePrice indicates that transformation on this variable may be needed prior to creating a model.   

![assign1_histogram_SalePrice_autobin](https://user-images.githubusercontent.com/49419673/148700091-49b5227a-3a9d-4540-baf8-540781b387e4.png)   ![qqplot saleprice](https://user-images.githubusercontent.com/49419673/148700121-ad626b6a-d2e1-479c-a3d9-94b05003f6d7.png)

#### Investigating NAs and Outliers
Missing Data   
The chart below shows variables with NA in the dataset. Several of them are due to houses not having certain features like basements, garages, fireplaces, or pools vs. data that is actually missing or mis-coded. The only instance of actual missing information is in the Electrical variable, where ID 1380 has Nan when its Utilities field lists AllPub. 

NA Values   
Lot Frontage: 259  
Alley: 1369      
MsnVnrType: 8    
MsnVnrArea: 8   
BsmtQual:  37   
BsmtCond: 37   
BsmtExposure: 38   
BsmtFinType1: 37   
BsmtFinType2: 38   
Electrical: 1    
FireplaceQu: 690   
GarageType: 81   
GarageYrBlt: 81    
GarageFinish: 81   
GarageQual: 81   
GarageCond: 81   
PoolQc: 1453   
Fence: 1179    
MiscFeature: 1406    

Several variables should not be included for consideration when modeling due to the high number of NAs representing 40% or greater of the 1460 homes in the train sample: Alley, Fireplace Qu, PoolQc, Fence, Misc Feature  

Outliers in SalePrice  
There are 60 outliers in the higher range of SalePrice (prices >= $347,037.50) and of these, 11 are extreme outliers (prices >=$467,675).  

#### Other considerations for preprocessing the dataset prior to building a model to predict SalePrice  
None of the homes was removed from the training dataset (n=1460) during the EDA described on this project, however, edits to the dataset could be performed to more accurately reflect a typical seller’s experience. When reviewing the variables, SaleCondition criteria could be used to eliminate homes. One could limit the dataset to only include sales with Normal, AdjLand, Alloca, and Partial conditions as these reflect more common market conditions for the home selling process. The conditions Abnorml and Family do not reflect the typical sale experience as Abnormal sales reflect prices where the seller is in distress (i.e. foreclosure, short sale) and Family sales do not put the home on the public market.  
Total homes that would be removed due to sales with Abnormal or Family conditions: 121  

#### Predictors of SalePrice  
The correlation heatmap below displays the correlation between continuous variables and SalePrice. The variables with highest correlation include:  
OverallQual: 0.79  
GrLivArea (Above Ground Living Area): 0.71  
GarageArea: 0.62  

![corr_saleprice_contvar](https://user-images.githubusercontent.com/49419673/148700764-bfdb1050-6be9-4313-b546-ff14cb3f450b.png)

Scatterplots were created to explore the relationship between these variables and SalePrice. They reveal a potential linear relationship with SalePrice for all three variables.   
![scatter overall_qual saleprice](https://user-images.githubusercontent.com/49419673/148700821-3eeb95b0-a6fd-4a8c-adf4-8fb874715ab2.png)  ![scatter grlivearea saleprice](https://user-images.githubusercontent.com/49419673/148700827-6c30cdfe-42be-485a-9e62-189ba1b21507.png)  
![scatter garage_area saleprice](https://user-images.githubusercontent.com/49419673/148700843-38b98107-0a54-41ce-96ad-d3acbcbae55e.png)



Visual inspection of the GrLivArea and GarageArea reveals outliers at the higher values. For GrLivArea, values >4,000 square feet and for Garage Area, values > 1200 square feet may influence a regression line. 

I explored the sale condition of these outliers to understand if the sales conditions affected their lower sale prices:   
* 4 outliers with GrLivArea >4000 SqFt:  Normal sale condition (1)/Partial or Abnormal condition (3)  
* 5 outliers with Garage Area >1200 SqFt: Normal condition (2)/Partial condition (3)  

When tuning a model, it may be worthwhile to remove the outlier units that did not have Normal conditions as they may influence the model’s fit. Further exploration on categorical variables including SaleCondition is needed to assess other potential predictors of SalePrice.  

#### Feature Creation to Generate a New Predictor
A new feature TotalSqFtCalc (Total Square Feet Calculate) was created by adding TotalBsmtSF (Total Basement Square Feet) and GrLivArea (Above Ground Living Area). This feature was created to reflect a common criteria for homebuyers, the total square footage of the home. Real estate listings include this metric and it was not already included in the dataset. The correlation between TotalSqFtCalc and SalePrice is high at 0.78.  

#### Min-max scaling and Standard scaling on dependent variable SalePrice  
Min-Max Scaling and Standard Scaling were performed on SalePrice to mitigate issues with modeling since the range of SalePrice is wide ($720,100). The chart below shows the transformed minimum and maximum scale of SalePrice. The scale is wider with the Standard Scaler since the method doesn’t bind values to a specific range as compared to Min-Max which limits the scale from 0 to 1. Standard Scaling may be preferred for this model since it is less affected by outliers, and there are a small number of extreme outliers in SalePrice.  
|               |  Min | Max |
|-------------- | ---- | --- |   
| Min Max Scaler | 0.00 | 1.00 |    
| Standard Scaler  | -1.84 | 7.23 |    



