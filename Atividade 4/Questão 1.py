import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import StratifiedKFold
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import precision_recall_fscore_support


data = pd.read_csv('Skin_NonSkin.txt', header=None, names=['v1', 'v2', 'v3', 'class'], sep='\t')

data_x = data[['v1', 'v2', 'v3']].to_numpy()
data_y = data['class'].to_numpy()

skfold = StratifiedKFold(n_splits=100)
n_splits = skfold.get_n_splits(data_x, data_y)

score_fmetric_1 = np.array([])
score_fmetric_2 = np.array([])

for train_index, test_index in skfold.split(data_x, data_y):
  data_x_train, data_x_teste = data_x[train_index], data_x[test_index]
  data_y_train, data_y_teste = data_y[train_index], data_y[test_index]

  knn = KNeighborsClassifier(n_neighbors = 1, weights="distance", metric="euclidean")
  knn.fit(data_x_train, data_y_train)
  predict = knn.predict(data_x_teste)

  _, _, score_fmetric, _ = precision_recall_fscore_support(data_y_teste, predict)

  score_fmetric_1 = np.append(score_fmetric_1, score_fmetric[0])
  score_fmetric_2 = np.append(score_fmetric_2, score_fmetric[1])

#Letra A
max_1 = score_fmetric_1.max()
med_1 = round(np.average(score_fmetric_1), 5)
min_1 = round(score_fmetric_1.min(), 5)

max_2 = score_fmetric_2.max()
med_2 = round(np.average(score_fmetric_2), 5)
min_2 = round(score_fmetric_2.min(), 5)

print(f'Medida-F Classe 1\nMax: {max_1}\nMed: {med_1}\nMin: {min_1}')
print(f'Medida-F Classe 2\nMax: {max_2}\nMed: {med_2}\nMin: {min_2}')

#Letra B
plt.hist(score_fmetric_1)
plt.savefig('hist_class_1.png')
plt.hist(score_fmetric_2)
plt.savefig('hist_class_2.png')

#Letra C
dev_1 = np.std(score_fmetric_1)
dev_2 = np.std(score_fmetric_2)

confidence_interval_1_n = round(med_1 - (1.96 * dev_1), 5)
confidence_interval_1_p = round(med_1 + (1.96 * dev_1), 5)
confidence_interval_2_n = round(med_2 - (1.96 * dev_2), 5)
confidence_interval_2_p = round(med_2 + (1.96 * dev_2), 5)

print(f'Intervalo de confiança da Classe 1: {confidence_interval_1_n} - {confidence_interval_1_p}')
print(f'Intervalo de confiança da Classe 2: {confidence_interval_2_n} - {confidence_interval_2_p}')