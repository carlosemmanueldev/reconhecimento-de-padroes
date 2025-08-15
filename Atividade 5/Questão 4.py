import pandas as pd
import numpy as np
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import precision_recall_fscore_support
from sklearn.impute import SimpleImputer

cols = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal', 'num']

data = pd.read_csv('processed.hungarian.data', header=None, names=cols, sep=',')

data = data.replace('?', np.nan)

imputer = SimpleImputer(strategy='mean', missing_values=np.nan)
imputer = imputer.fit(data)
data.iloc[:,:] = imputer.transform(data)

data_x = data[cols[:-1]].to_numpy()
data_y = data['num'].to_numpy()

stratified = StratifiedShuffleSplit(n_splits=100, test_size= 0.1)

data_scores = np.array([])

for train_index, test_index in stratified.split(data_x, data_y):
  data_x_train, data_x_test = data_x[train_index], data_x[test_index]
  data_y_train, data_y_test = data_y[train_index], data_y[test_index]
  
  knn = KNeighborsClassifier(n_neighbors = 1, weights="distance", metric="euclidean")
  knn.fit(data_x_train, data_y_train)
  
  predict = knn.predict(data_x_test)

  precision, recall, fscore, support = precision_recall_fscore_support(data_y_test, predict)

  data_scores = np.append(data_scores, fscore)
  
med_1 = np.average(data_scores)
dev_1 = data_scores.std()

confidence_interval_1_n = round(med_1 - (1.96 * dev_1), 5)
confidence_interval_1_p = round(med_1 + (1.96 * dev_1), 5)

print(f'Intervalo de confiança da taxa de acerto: {confidence_interval_1_n}   {confidence_interval_1_p}')