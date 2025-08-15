import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import preprocessing
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler

cols = ['class', 'alcohol', 'malic_acid', 'ash', 'alcalinity_of_ash', 'magnesium', 'total_phenols', 'flavanoids', 'nonflavanoid_phenols', 'proanthocyanins', 'color_intensity', 'hue', 'OD280/OD315_of_diluted_wines', 'proline']

data = pd.read_csv('wine.data', header=None, names=cols)

data_x = data[cols[1:]]
data_y = data['class']

#original
data_scores = []

for i in range(100):
  data_train_x, data_test_x, data_train_y, data_test_y = train_test_split(data_x, data_y, test_size=0.5)

  knn = KNeighborsClassifier(n_neighbors = 1, weights="distance", metric="euclidean")
  knn.fit(data_train_x, data_train_y)

  predict = knn.predict(data_test_x)
  data_score = knn.score(data_test_x, data_test_y)
  data_scores = np.append(data_scores, data_score)

med = np.average(data_scores)
dev = data_scores.std()

confidence_interval_n = round(med - (1.96 * dev), 5)
confidence_interval_p = round(med + (1.96 * dev), 5)

print(f'Intervalo de confiança da taxa de acerto: {confidence_interval_n}   {confidence_interval_p}')

#ajustado para [0, 1]

scaler = MinMaxScaler(feature_range=(0,1))
scaled_data = scaler.fit_transform(data_x)

data_scores = []

for i in range(100):
  data_train_x, data_test_x, data_train_y, data_test_y = train_test_split(scaled_data, data_y, test_size=0.5)

  knn = KNeighborsClassifier(n_neighbors = 1, weights="distance", metric="euclidean")
  knn.fit(data_train_x, data_train_y)

  predict = knn.predict(data_test_x)
  data_score = knn.score(data_test_x, data_test_y)
  data_scores = np.append(data_scores, data_score)

med = np.average(data_scores)
dev = data_scores.std()

confidence_interval_n = round(med - (1.96 * dev), 5)
confidence_interval_p = round(med + (1.96 * dev), 5)

print(f'Intervalo de confiança da taxa de acerto ajustado para [0, 1]: {confidence_interval_n}   {confidence_interval_p}')

#padronizado

scaler = StandardScaler()
scaled_data = scaler.fit_transform(data_x)

data_scores = []

for i in range(100):
  data_train_x, data_test_x, data_train_y, data_test_y = train_test_split(scaled_data, data_y, test_size=0.5)

  knn = KNeighborsClassifier(n_neighbors = 1, weights="distance", metric="euclidean")
  knn.fit(data_train_x, data_train_y)

  predict = knn.predict(data_test_x)
  data_score = knn.score(data_test_x, data_test_y)
  data_scores = np.append(data_scores, data_score)

med = np.average(data_scores)
dev = data_scores.std()

confidence_interval_n = round(med - (1.96 * dev), 5)
confidence_interval_p = round(med + (1.96 * dev), 5)

print(f'Intervalo de confiança da taxa de acerto padronizado: {confidence_interval_n}   {confidence_interval_p}')