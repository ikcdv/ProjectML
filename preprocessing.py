

#%%
from import_data import *
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import numpy as np
import pandas as pd



df_train, df_test, df_train_labels = data_load()
data = [df_train, df_test, df_train_labels]
names = ["df_train", "df_test", "df_train_labels"]

#standardscaller
#pca 
#oversampling/undersampling

X = df_train
y = df_train_labels

X_train, X_test, y_train, y_test = train_test_split(X, y , random_state=0, stratify = y)


pca = PCA(n_components = 2, whiten = True)

X_train_standarized = StandardScaler().fit_transform(X_train)
X_test_standarized = StandardScaler().fit_transform(X_test)

X_train_pca = pca.fit_transform(X_train_standarized)
X_test_pca = pca.fit_transform(X_test_standarized)

print('Original shape: {}'.format(str(X_train_standarized.shape)))
print('Reduced shape: {}'.format(str(X_train_pca.shape)))
print('Shape componets PCA: {}'.format(pca.components_.shape))


print('Componets PCA: \n{}'.format(pca.components_))

X_train_pca = pd.DataFrame(X_train_pca, columns = ['c1', 'c2'])
X_train_pca = X_train_pca.assign(labels=(y_train).values)
X_train_pca.sample(5)

X_train_pca[['c1', 'c2']].describe()

X_train_pca['labels'].sample(5)


plt.figure(figsize=(15, 15))
sns.scatterplot(data = X_train_pca, x = 'c1', y='c2', hue = X_train_pca['labels'], palette = ['green', 'red'])
# %%
