import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_recall_fscore_support
from sklearn.metrics import accuracy_score

cols = ['class', 'alcohol', 'malic_acid', 'ash', 'alcalinity_of_ash', 'magnesium', 'total_phenols', 'flavanoids', 'nonflavanoid_phenols', 'proanthocyanins', 'color_intensity', 'hue', 'OD280/OD315_of_diluted_wines', 'proline']

data = pd.read_csv('wine.data', header=None, names=['class', 'alcohol', 'malic_acid', 'ash', 'alcalinity_of_ash', 'magnesium', 'total_phenols', 'flavanoids', 'nonflavanoid_phenols', 'proanthocyanins', 'color_intensity', 'hue', 'OD280/OD315_of_diluted_wines', 'proline'])
data_train_x, data_test_x, data_train_y, data_test_y = train_test_split(data[cols[1:]], data['class'], test_size=0.3)

knn = KNeighborsClassifier(n_neighbors = 1)

knn.fit(data_train_x, data_train_y)

predict = knn.predict(data_test_x)

confusionMatrix = confusion_matrix(data_test_y, predict)

print('Matriz de confusão:\n', confusionMatrix)

precision, recall, fscore, support = precision_recall_fscore_support(data_test_y, predict)

accuracy = accuracy_score(data_test_y, predict)

print('\nPrecisão:', precision)
print('Recall:', recall)
print('Medida-F:', fscore)
print('Taxa de acerto:', accuracy)

