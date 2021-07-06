

#%%
from import_data import *
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
import pandas as pd

df_train, df_test, df_train_labels = data_load()
data = [df_train, df_test, df_train_labels]
names = ["df_train", "df_test", "df_train_labels"]

X = df_train
y = df_train_labels
X_train, X_test, y_train, y_test = train_test_split(X, y , random_state=0, stratify = y)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

pca = PCA(n_components=2)
X_train_pca = pca.fit_transform(X_train_scaled)
X_test_pca = pca.transform(X_test_scaled)

print('Original shape: {}'.format(str(X_train_scaled.shape)))
print('Reduced shape: {}'.format(str(X_train_pca.shape)))
print('Shape componets PCA: {}'.format(pca.components_.shape))
print('Componets PCA: \n{}'.format(pca.components_))

df_pca = pd.DataFrame(data = X_train_pca, columns = ['c1', 'c2'])
df_final = pd.concat([df_pca, y_train], axis = 1)
df_final.columns = ['c1', 'c2', 'labels']
df_final.sample(5)

plt.figure(figsize=(15, 15))
sns.scatterplot(data = df_final, x = 'c1', y='c2', 
hue = df_final['labels'], palette = ['green', 'red'])

plt.savefig('plot.png')

# %%
