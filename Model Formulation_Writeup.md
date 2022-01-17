# Ames Housing Data

### Data Preprocessing and Explanatory Data Analysis

The train dataset was pre-processed to handle missing values and encode categorical variables with dummy variables. Missing values for continuous and categorical variables were imputed with a 0 value, since the NA value indicated that the feature was not present (i.e. Fireplaces NA indicated the home did not have a fireplace. Categorical variables were encoded in 2 ways:
* Categorical features with ordinal values (i.e. KitchenQual values ranged from Excellent to Poor or NA)  were imputed with a scale from 0 (NA) to 5 (Excellent) to preserve the ordinal scale
* Categorical features without ordinal values were preprocessed to create binary dummy variables to indicate the presence of the feature. For example, SaleCondition could take on values like Abnormal or Normal, and homes with these values were processed to create new features, such as SaleCondition_Normal.

After preprocessing the dataset included 256 features.

Exploratory data analysis reviewed features with the strongest and lowest correlations with SalePrice (correlations ranging 0.79 – 0.23 and -0.20 t0 -0.41) as well as running the Variance Inflation Factors on these features to learn which features had high correlations amongst others in the dataset to minimize multicollinearity in the model. Features that did not make the correlation cutoff and that had high VIF scores (above 15) were removed, which reduced the set of features to 78. An additional feature ‘TotalSqftCalc’ was created to consolidate features capturing square footage, ‘GrLivArea’ and’TotalBsmtSf.’ 

VIF was run again on the set of 79 features, and an additional 5 features were removed to bring the total features to 72 features. 

EDA also included plots of 10 features with the highest correlation to SalePrice. Plots on GrLivArea and OverallQual, revealed 2 outlier homes below that had lower SalePrice relative to their higher square footage and quality score. After removing the 2 outlier homes, the dataset included 1458 values with 72 features.

![pairplots 3_readme](https://user-images.githubusercontent.com/49419673/149709656-3843d394-95ea-4731-96bd-a7a002dd4d93.png)

An initial linear regression model (Model 1) was run to assess which features would include statistically significant coefficients with a p-value <0.1, indicating evidence of a linear association with SalePrice. The initial model summary showed that over half of the features did not have coefficients that were statistically significant, so all features with a p-value <0.1 were removed, reducing the feature set to 33. 

### Model Evaluation
Based on the initial model, 3 types of linear regression models were further explored with the 33 features:
* Model 2: No scaling
* Model 3: Min-Max Scaling to better deal with outlier values across SalePrice and features
* Model 4-5: Data was processed with Min-Max scaling and 2 types of Polynomial Features, raised to the 2nd and 3rd powers

After the preprocessing and EDA, the dataset was split into train and test groups to test the various models by allocating 80% of the dataset to the train group and 20% to the test group. The test groups were used to validate the models using the metric root mean squared error (RMSE) from the Kaggle competition. RMSE provides a measure of how well the model fits the data by measuring the average distance between the predicted values and actual values. Below is a chart showing RMSE across the 4 models. Model 3, which used the MinMax scaler achieved the lowest RMSE. Model 4 with the features raised to the 2nd power achieved the next lowest RMSE, which Model 2 with no scaling had the highest RMSE at over 27,000. 

|       | Model 2 - no scaling | Model 3 - MinMax scaler | Model 4 - Polynomial degree: 2 | Model 5 - Polynomial degree:3 |
| ----- | -------------------- | ----------------------- | ------------------------------ | ----------------------------- |
| RMSE  | 27,093.0192          | 0.0483                  | 0.0813                         | 0.5135                        |

K-Fold Cross validation was also used to explore the range of RMSE that could be achieved on Model 3 with Min-Max scaling. Below is the list of RMSE values achieved after splitting the training and test sets into 5 groups:
* -0.0556
* -0.0635
* -0.0511
* -0.0542
* -0.0449

The plots below provide visualizations of the goodness of fit for Model 2 and Model 3 by allowing a comparison on the residuals after scaling the data in Model 3.
The Q-Q Plot for Model 3 shows increased normality of the residuals, however the data still skews upward on the back half.

![model2 actualvpred](https://user-images.githubusercontent.com/49419673/149710513-fdccdd39-3caa-4586-8b1e-50c3b3ceb3c9.png)
![model2 residuals](https://user-images.githubusercontent.com/49419673/149710533-280fb7bf-bea6-4e32-a115-ec4020fb4ccb.png)
![model2 qqplot](https://user-images.githubusercontent.com/49419673/149710539-2a1879b5-0b8a-4c8e-a8ea-0eefad9f7f3c.png)

![scaler_actual vs predicted model3](https://user-images.githubusercontent.com/49419673/149710573-a4cba4f8-d16d-4b90-bc98-7e0d8f79fcd5.png)
![scaler_residuals model3](https://user-images.githubusercontent.com/49419673/149710590-40176afc-1130-4c59-b15f-417e82032368.png)
![scaler_qqplot model3](https://user-images.githubusercontent.com/49419673/149710607-66a5aa9b-316d-4dbe-b9b2-3b7192cb3323.png)

The comparison of RMSE in the train and test groups when fitting Models 4 and 5 suggest that underfitting is occurring and that polynomial features may not provide the best fit. The train RMSE for Models 4 and 5 were Model 4: 0.0326 and Model 5: 0.0. 

### Insights from the models
The coefficients from Model 3 provide indicators of which features have statistically significant impact on SalePrice. These features include:
* OverallCond
* Garage_Area
* TotRmsAbvGrd
* BedroomAbvGr
* Fireplaces
* BsmtFullBath
* Lot_Area
* House_Style_2Story
* Neighborhood_NridgHt
* BsmtCond
* PoolQC
* TotalSqftCalc
* MasVnrArea

