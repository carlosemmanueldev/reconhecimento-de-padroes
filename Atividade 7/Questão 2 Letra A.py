import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn_extra.cluster import KMedoids

cols = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']

data = pd.read_csv('iris.data', header=None, names=cols)

data_x = data[cols[:-1]]
data_y = data['class']

# Dividindo a base estratificada com holdout 50/50
x_train, x_test, y_train, y_test = train_test_split(data_x, data_y, test_size=0.5, stratify=data_y)

# Instanciando o algoritmo K-Medoids e executando no conjunto de treinamento.
kmedoids = KMedoids(n_clusters=9, max_iter=10, random_state=1)

y_predicted = kmedoids.fit_predict(x_train)

print(y_predicted)