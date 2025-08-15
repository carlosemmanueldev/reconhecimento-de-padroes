import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

cols = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']

data = pd.read_csv('iris.data', header=None, names=cols)

data_x = data[cols[:-1]]
data_y = data['class']

#Cria o modelo de k-médias com k=5
kmeans = KMeans(n_clusters=5, random_state=1)
kmeans.fit(data_x)
data['group'] = kmeans.labels_

#Calcula a quantidade de elementos de cada classe em cada grupo
group_class_count = data.groupby(['group', 'class']).size().unstack(fill_value=0)

#Cria os gráficos
fig, axs = plt.subplots(1, 5, figsize=(15,5))
for i in range(5):
    axs[i].bar(['Setosa', 'Versicolor', ' Virginica'], group_class_count.iloc[i])
    axs[i].set_title(f'Grupo {i}')
    axs[i].set_ylim([0, max(group_class_count.sum(axis=1))+2])
    axs[i].set_xlabel('Classe')
    axs[i].set_ylabel('Quantidade')
   
plt.tight_layout()
plt.show()