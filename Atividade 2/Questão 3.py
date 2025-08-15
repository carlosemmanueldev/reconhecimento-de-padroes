import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

data = pd.read_csv('iris.data.train', header=None, names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])
data_test = pd.read_csv('iris.data.test', header=None, names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])

neigh = KNeighborsClassifier(n_neighbors=1)
neigh.fit(data[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']], data['class'])

neigh.predict(data_test[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']])

print("Taxa de acerto: ", neigh.score(data_test[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']], data_test['class']))
