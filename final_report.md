# Project Machine Learing Raport 

#### Team: Iwona Karpicka, Michał Ogrodowicz


## 1. Research problem
The data consists of 2 splits train_data.csv and test_data.csv. There are numeric observations labelled either -1 or +1. Labels for the training data are located in in train_labels.csv. 
The aim of the project is to predict labels for the testing data.

Desired output:
Save predictions in test_labels.csv,
Prepare a report (saved as report.md)with the explanations on how you came up with the solution. What obstacles you faced and how did you solve them. Add also information about data quality and so on.

## 2. Data analysis
### 2.1. Data information
Both the df_train and df_test datasets contain the same number of columns. The data consists of negative and positive values and there is no empty value. The data in each column is very different, so the basic statistics are different. 

### 2.2. Distribution
Each of the columns also has outliers that vary widely. This is also shown by kurtosis. positive kurtosis shows that there are more positive outliers in the data than there is for a normal distribution. In contrast, negative kurtosis indicates that there are fewer positive outliers in the data than in the case of a normal distribution. There is no normal distribution in the columns because kurtosis is different from zero. Normal distribution is not symmetrical, no values ​​equal to 0 in skew. This is also confirmed by the charts. The hypotheses about the normal distribution for each feature were rejected.

### 2.3. Problem
The collection consists of many columns. No correlation was performed for the data due to multiple columns. Binary classification. The statistics showed that the data for all communities are not homogeneous and balanced. 

## 3. Preprocessing
### 3.1 Tools
The train_data set has been split using test_train_split.StnadardScaler was used due to the presence of outliers. The data was standardized and reduced to two dimensions to show clustering in the graph. The generated graph does not show the correlation between the points.

* test_train_split
* StandardScaler
* PCA(n_components=2)
* scatterplot

### 3.2 Problem
No division into clusters.

## 4. Models
### 4.1 Baseline model
For the base model was selected DummyClassifier A DummyClassifier is a type of classifier which does not generate any insight about the data and classifies the given data using only simple rules. So, it is used only as a simple baseline for the other classifiers
Received results:
![4..1](4.1.PNG)

### 4.2 Model
For the model proper, we have established 3 classifiers:
 - DecisionTreeClassifier()
 - KNeighborsClassifier(3)
 - SVC()
Received:
![](4.2.PNG)

All classifiers were better than the base model. The classifier DecisionTreeClassifier was the worst. The best classifiers were SVC and KNeighborsClassifier with number of 3 neighbors. 

### 4.3 Boosting
 2 boosting algorithms were tried:
 - AdaBoostClassifier()
 - lgb.LGBMClassifier()
AdaBoostClassifier is a method whereby one better can be obtained from a large number of weak classifiers.  LightGBM is a fast, distributed, high performance gradient boosting framework based on decision tree algorithms.
The result was obtained without and with parameters. Parameters were determined by pipeline.
Received without parameters:
![](adabez.PNG)

![](lgbez.PNG)

 - AdaBoostClassifier() - 'n_estimators': [50, 100, 150], 'learning_rate': [0.1, 0.01, 0.05]}]
 - lgb.LGBMClassifier() - 'num_leaves': [7, 15, 31], 'max_depth': [3, 4, 5]
Received with parameters:
![](adaz.PNG)

![](lz.PNG)

Due to obtaining 1.0 for f1_score LightGBM with parameters, the remaining statistics were calculated. As a last resort, AdaBoostClassifier was used for the final model. 
![](iz2.PNG)

### 4.4  Final model
These parameters were used in final model with others classifiers. The final pipeline had parameters choosen earlier. In the pipeline selected:
 - PCA(n_components = 0.99)
 - StandardScaler()
 - SVC()
 
 In the search_space. Parameters in accordance with point 4.3:
 - KNeighborsClassifier()
 - AdaBoostClassifier()

GridSearchCV used to select the best model. The result is at a high level:
Best score: 0.975 
TN: 100
FP: 13
FN: 24
TP: 988
![](final.png)!

### 4.5 Data
The data was written to a file labels.csv

### 4.6 Problems
The methods are time-consuming and do not always produce better results. 
