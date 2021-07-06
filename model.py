from import_data import *
import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.dummy import DummyClassifier
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
from sklearn import svm
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
import io


df_train, df_test, df_train_labels = data_load()
data = [df_train, df_test, df_train_labels]
names = ["df_train", "df_test", "df_train_labels"]

X = df_train
y = df_train_labels
X_train, X_test, y_train, y_test = train_test_split(X, y , random_state=0, stratify = y)

strategies = ['stratified', 'most_frequent', 'prior', 'uniform']

for i in strategies:
    dummy_clf = DummyClassifier(strategy=i)
    dummy_clf.fit(X_train, y_train)
    score = dummy_clf.score(X_train, y_train)
    dum_labels = np.unique(dummy_clf.predict(X))
    print(f'For {i} strategy score is {score}')
    plt.bar(i, score)

    scaler = StandardScaler()

X_train_scale = scaler.fit_transform(X_train)
y_train_scale = scaler.fit_transform(y_train)

pca = PCA(n_components=2, whiten=True)
X_pca = pca.fit_transform(X_train_scale)

clf = LogisticRegression(random_state=0).fit(X, y)


knn = KNeighborsClassifier().fit(X, y)

svc = svm.SVC()
svc.fit(X, y)

rnf = RandomForestClassifier().fit(X, y)

pipe = Pipeline([('pca', pca), ('scaler', scaler),
('classifier', SVC())
])

search_space = [{'scaler': [StandardScaler()],
                'pca': [PCA()]},
                {'classifier': [SVC()],
                 'classifier__kernel': ['linear', 'rbf'],
                 'classifier__class_weight': [None, 'balanced'],
                 'classifier__gamma': ['scale', 'auto'],
                 'classifier__C': np.logspace(1,4,10)},
                {'classifier': [KNeighborsClassifier()],
                 'classifier__n_neighbors': [1, 2, 5],
                 'classifier__algorithm': ['auto']}]

                

grid_search = GridSearchCV(pipe,
                           search_space,
                           cv=5,
                           verbose=2,
                           n_jobs=-2,
                           scoring='balanced_accuracy')

best_model = grid_search.fit(X, y.values)

print(best_model.best_estimator_)
print("The mean accuracy of the model is:",best_model.score(X, y))


