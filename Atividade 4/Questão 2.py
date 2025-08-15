import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import precision_recall_fscore_support as score

cols = ['class', 'alcohol', 'malic_acid', 'ash', 'alcalinity_of_ash', 'magnesium', 'total_phenols', 'flavanoids', 'nonflavanoid_phenols', 'proanthocyanins', 'color_intensity', 'hue', 'OD280/OD315_of_diluted_wines', 'proline']


data = pd.read_csv('wine.data', header=None, names=['class', 'alcohol', 'malic_acid', 'ash', 'alcalinity_of_ash', 'magnesium', 'total_phenols', 'flavanoids', 'nonflavanoid_phenols', 'proanthocyanins', 'color_intensity', 'hue', 'OD280/OD315_of_diluted_wines', 'proline'])

data_x = data[cols[1:]]
data_y = data['class']

data_without = pd.read_csv('wine.data', header=None, names=['class', 'alcohol', 'malic_acid', 'ash', 'alcalinity_of_ash', 'magnesium', 'total_phenols', 'flavanoids', 'nonflavanoid_phenols', 'proanthocyanins', 'color_intensity', 'hue', 'OD280/OD315_of_diluted_wines', 'proline'])

data_without_x = data[cols[1:-1]]
data_without_y = data['class']

data_scores = []
data_scores_without = []

for i in range(100):
  data_train_x, data_test_x, data_train_y, data_test_y = train_test_split(data_x, data_y, test_size=0.5)

  knn = KNeighborsClassifier(n_neighbors = 1, weights="distance", metric="euclidean")
  knn.fit(data_train_x, data_train_y)

  predict = knn.predict(data_test_x)
  data_score = knn.score(data_test_x, data_test_y)
  data_scores = np.append(data_scores, data_score)

  data_without_train_x, data_without_test_x, data_without_train_y, data_without_test_y = train_test_split(data_without_x, data_without_y, test_size=0.5)

  knn_without = KNeighborsClassifier(n_neighbors = 1, weights="distance", metric="euclidean")
  knn_without.fit(data_without_train_x, data_without_train_y)

  predict_without = knn_without.predict(data_without_test_x)
  data_score_without = knn_without.score(data_without_test_x, data_without_test_y)
  data_scores_without = np.append(data_scores_without, data_score_without)


#Letra A
print(f'Diferença das 100 taxas de acerto:\n{data_scores - data_scores_without}')

#Letra B
med = np.average(data_scores - data_scores_without)
dev = np.std(data_scores - data_scores_without)

confidence_interval = round(med - (1.96 * dev), 5)
confidence_interval_w = round(med + (1.96 * dev), 5)

print(f'Intervalo de confiança: {confidence_interval}   {confidence_interval_w}')

#Letra C
med_1 = np.average(data_scores)
dev_1 = data_scores.std()

confidence_interval_1_n = round(med_1 - (1.96 * dev_1), 5)
confidence_interval_1_p = round(med_1 + (1.96 * dev_1), 5)

print(f'Intervalo de confiança da taxa de acerto da base completa: {confidence_interval_1_n}   {confidence_interval_1_p}')

med_without = np.average(data_scores_without)
dev_without = data_scores_without.std()

confidence_interval_without_1_n = round(med_without - (1.96 * dev_without), 5)
confidence_interval_without_1_p = round(med_without + (1.96 * dev_without), 5)

print(f'Intervalo de confiança da taxa de acerto da base sem a ultima coluna: {confidence_interval_without_1_n}   {confidence_interval_without_1_p}')