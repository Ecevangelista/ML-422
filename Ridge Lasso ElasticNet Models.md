# Ames Housing Data Model Exploration

#### Summary of Previous Data Preprocessing and Explanatory Data Analysis

The train dataset was pre-processed to handle missing values and encode categorical variables with dummy variables. Missing values for continuous and categorical variables were imputed with a 0 value, since the NA value indicated that the feature was not present (i.e. Fireplaces NA indicated the home did not have a fireplace. Categorical variables were encoded in 2 ways:  
* Categorical features with ordinal values (i.e. KitchenQual values ranged from Excellent to Poor or NA)  were imputed with a scale from 0 (NA) to 5 (Excellent) to preserve the ordinal scale
* Categorical features without ordinal values were preprocessed to create binary dummy variables to indicate the presence of the feature. For example, SaleCondition could take on values like Abnormal or Normal, and homes with these values were processed to create new features, such as SaleCondition_Normal.

The train dataset was edited to remove features with high Variance Inflation Factors to minimize multicollinearity in the model. Additionally 3 new features were created by consolidating other features:  
* TotalSqftCalc: Sum of square footage from GrLivArea and TotalBsmtSf
* TotalBathroomAbv: Sum of FullBath and HalfBath
* TotalBathroomBelow: Sum of BsmtFullBath and BsmtHalfBath

After removing features with high VIF and adding 3 new features, total features to be included in the model: 36  

Plots on GrLivArea and OverallQual, revealed 2 outlier homes that had lower SalePrice relative to their higher square footage and quality score. After removing the 2 outlier homes, the dataset included 1458 values.   

#### Model Comparison and Evaluation

Four models were created to evaluate different regression algorithms: Ridge Regression, Lasso Regression, Elastic Net, and Elastic Net with hyperparameters tuned.
Additionally, the Lasso Regression and Elastic Net with tuned hyperparameters models also incorporated K-Fold cross validation to optimize the lowest RMSE score. GridSearchCV yielded the optimal alpha at 0.001 and optimal L1 ratio at 0.2.

ElasticNet with the hyperparameters tuned to alpha = 0.001 and L1_ratio = 0.2 produced the lowest RMSE at 21,638.7. In comparison, the ElasticNet model that used the default alpha and L1 ratio, produced the highest RMSE at 47,620.6. Model 4’s low alpha of 0.001 indicate that the penalty applied is close to approximating ordinary least squares regression and the model’s lower L1 ratio of 0.2 applies a penalty more in line with ridge regression.  

|      | #1: Ridge Regression | #2: LassoCV | #3: ElasticNet            | #4 Elastic Net with Hyperparameters Tuned |
| -----| -------------------- | ----------- | --------------------------| ------------------------------------------|                    
|      | Alpha = 0.5          |             | Alpha = 1, L1 ratio = 0.5 | Alpha = 0.001, L1 ratio = 0.2             |
| RMSE | 25,984.3             | 25,631.9    | 47,620.6                  | 21,638.7                                  | 

Goodness of Fit Plots
The Ridge and Lasso regression plots look very similar, and the residual plots corroborate the similar values of RMSE. Conversely, Model 3 Elastic Net plots are the most distinct, with the model underfitting the actual values and the QQ plot showing the residual errors to have less normality than in the other plots. 

![Ridge Regression Actual vs Fitted](https://user-images.githubusercontent.com/49419673/150708784-f907de96-daff-48eb-9d71-d4120c371573.png)
![Ridge Regression Residual Plot test](https://user-images.githubusercontent.com/49419673/150708797-8d34d11c-3d48-48b4-aab9-15fdbb220e4f.png)
![Ridge Regression QQ Plot test](https://user-images.githubusercontent.com/49419673/150708805-ad72750d-6293-45f5-b2df-91f1c2de0710.png)

![Lasso CV Actual vs Fitted](https://user-images.githubusercontent.com/49419673/150708837-66e5a0ff-1c7c-47e3-838b-85f7e81ef2a6.png)
![LASSO CV Residual Plot test](https://user-images.githubusercontent.com/49419673/150708848-365552c0-4a72-4729-b99c-3776874172fb.png)
![Lasso CV QQ Plot Test](https://user-images.githubusercontent.com/49419673/150708855-0794b844-15c5-4d84-bffc-28230b14cfcb.png)

![3_Elastic Net Actual vs predicted](https://user-images.githubusercontent.com/49419673/150708893-45352bfa-51bd-48ef-8c34-c9b0c26f949b.png)
![3_Elastic Net residual plot](https://user-images.githubusercontent.com/49419673/150708908-a111cb29-8bbb-4ea2-b083-df40eac2de11.png)
![3_Elastic Net QQ plot](https://user-images.githubusercontent.com/49419673/150708920-18688a1a-186a-4c1b-9772-be21f14ddbe7.png)

![Elastic Net Tuned Actual vs Fitted](https://user-images.githubusercontent.com/49419673/150708966-ee89614d-7f46-4ab7-9f5a-3a2d40927b5e.png)
![Elastic Net Tuned Residual plot](https://user-images.githubusercontent.com/49419673/150708983-60b6c6e5-218d-467d-955a-a7991c873704.png)
![Elastic Net Tuned QQ plot](https://user-images.githubusercontent.com/49419673/150708992-a3967ac8-c00b-4aa6-985c-6f9cddc91d9f.png)

#### Interpreting the Models

Models 1 and 2 contain a similar set of features for those that have the highest weight positively and negatively impacting SalePrice. TotalSqftCalc, OverallQual, LotArea, and MasVnrArea are among the top features to positively impact SalePrice.   

Model 4  also has a similar list of top features, but differs by also prioritizing neighborhood features like Neighorhood_StoneBr and Neighborhood_NrigHt. Additionally, Model 4 places more weight on features associated with the garage than any of the other models by including GarageType_BuiltIn, GarageArea, and GarageType_Attchd in the top 10 features. Model 3 behaves very differently as seen in its RMSE and goodness of fit plots by placing the most weight on features related to quality scores: FireplaceQu, KitchenQual, ExterQual, OverallQual, and HeatingQC.  

#1 Ridge Regression Weights

![Ridge weights](https://user-images.githubusercontent.com/49419673/150709143-2c1fff56-8071-4603-9814-d6d21e5b1bde.png)

#2 Lasso Regression Weights

![Lasso CV weights](https://user-images.githubusercontent.com/49419673/150709189-abe05b6c-b76c-4502-8654-c00e266c1bfc.png)

#3 ElasticNet Regression Weights Alpha = 1, L1 ratio = 0.5

![3_Elastic Net Weights](https://user-images.githubusercontent.com/49419673/150709290-b4fde50c-d698-4fda-814d-e43bbbd00661.png)

#4 ElasticNet Regression with Hypertuned Parameters Alpha = 0.001, L1 ratio = 0.2

![4_Elastic Net Tuned weights](https://user-images.githubusercontent.com/49419673/150709369-c14c8093-0453-47bd-96b0-d107f06f5e70.png)





