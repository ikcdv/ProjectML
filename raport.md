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

### 4. Models

