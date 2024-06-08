# SyriaTel  Customer churn

### INTRODUCTION 
In the current world of business, customer satisfaction has become an integral part for business success. We will be using CRISP-DM methodology in trying to find a solution for our stakeholders at SyriaTel in order to find a solution for customer churning
In the following sections, we will detail the steps involved in developing classification models, from data preparation, to model training, evaluation, and deployment with the goal to provide a comprehensive, actionable solution that empowers Syriatel to reduce churn and sustain its growth in the competitive telecom landscape

The project structure is as follows:
1. Business Understanding
2. Data Understanding
3. Data Preparation
4. Explaratory Data Analysis
5. Modeling 
6. Model Evaluation
7. Recomendations and Conclusions

### 1. Business Understanding
SyriaTel company is a telecomunication company focused on being one the best in providing quality services to its customers and therefore they need to be competetive and be aware of there customers dynamics and preferences. 

Although such efforts have been fruitful over the years, the company needs to increase its commitment to reducing customer charning rates, which might threaten its market position, profitability, and overall growth. Retaining customers will increase the company's net profits by reducing costs involved in lossing customers.

### 2. Data Understanding
our dataset has 21 features namely:
• State: The state the customer lives in
• Account Length: The number of days the customer has had an account.
• Area Code: The area code of the customer
• Phone Number: The phone number of the customer
• International Plan: True if the customer has the international plan, otherwise false.
• Voice Mail Plan: True if the customer has the voice mail plan, otherwise false.
• Number Vmail Messages: the number of voicemails the customer has sent.
• Total Day Minutes: total number of minutes the customer has been in calls during the day.
• Total Day Calls: total number of calls the user has done during the day.
• Total Day Charge: total amount of money the customer was charged by the Telecom company for calls during the day.
• Total Eve Minutes: total number of minutes the customer has been in calls during the evening.
• Total Eve Calls: total number of calls the customer has done during the evening.
• Total Eve Charge: total amount of money the customer was charged by the Telecom company for calls during the evening.
• Total Night Minutes: total number of minutes the customer has been in calls during the night.
• Total Night Calls: total number of calls the customer has done during the night.
• Total Night Charge: total amount of money the customer was charged by the Telecom company for calls during the night.
• Total Intl Minutes: total number of minutes the user has been in international calls.
• Total Intl Calls: total number of international calls the customer has done.
• Total Intl Charge: total amount of money the customer was charged by the Telecom company for international calls.
• Customer Service Calls: number of calls the customer has made to customer service.
• Churn: true if the customer terminated their contract, otherwise false

### 3. Data Preparation
Our data was almost clean when we look at missing values and duplicates. We also checked for outliers and treated outliers by removing then since they are sensitive to modeling

### 4. EDA
##### Bivariate Analysis
After treating our dataset, we removed majority of the outliers and performed binary and multivariable analysis to see what our data communicates before building the prediction models.The graph on our index.ipynb shows the churning rate at every state with Nj having the highest rate and Hi having the lowest

#### Multivariate Analysis
We looked at the correlation between our features with 1 and -1 showing very high correlation and 0 showing no correlation

### 5. Modeling
For Modeling we built 3 models:
                  1. logistic Regression
                  2. K-Nearest Neighbors
                  3. Decision Tree Classifier
1. Logistic Regression
For the first model we a built a base logistic Regression that had a test accuracy score of of 88% but in terms of predicting the minority(Churned class) it was not one of the best
We had to improve by addressing the class imbalance which did well in predicting theminority class but test accuracy dropped to 76%

2. K-Nearest Neighbors
For the second model we a built a base KNearest Neighbor that had a test accuracy score of of 87% which is quite nice
We tried to improve by introducing Grid search and hyperparameter tuning to get the best parameters for our model. We tested a new KNN model with the best parameters and the new accuracy rose to 88% which was amazing

3. Decision Tree Classifier
For the Third model we a built a base Decision Tree classifier that had a test accuracy score of of 91% which is the best compared to the previous 2 model
We tried to improve by introducing Grid search and hyperparameter tuning to get the best parameters for our model. We tested a new Decision Tree classifier model with the best parameters and the new accuracy rose to 95% which was amazing

##### Model Evaluation 
here we evaluated every model by looking at the confusion matrics, f1-score, model precision recall and we compared all the models from the evaluation results and from this we concluded that Decision Tree Classifier outperformed all the others in predicting whether a customer will churn or not 

### 6. Recommendation and Conclusion
1.I would recommend SyriaTel communication to use Decision tree Model in predicting whether a customer will churn or not therefore reducing the cost of trying to retain customers
2.Put new strategies in place such as marketing and advertising in states like NJ, SC and TX to reduce churning rate and increase market
reach
3.Maintain the same strategies of retaining customers in states like HI, AK and AZ since churning rate is very low