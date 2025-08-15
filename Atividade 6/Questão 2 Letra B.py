import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from keras.models import Sequential
from keras.layers.core import Dense, Activation

cols = ['class', 'alcohol', 'malic_acid', 'ash', 'alcalinity_of_ash', 'magnesium', 'total_phenols', 'flavanoids', 'nonflavanoid_phenols', 'proanthocyanins', 'color_intensity', 'hue', 'OD280/OD315_of_diluted_wines', 'proline']

data = pd.read_csv('wine.data', header=None, names=cols)

data_x = data[cols[1:]]
data_y = data['class']

lb = preprocessing.LabelBinarizer()
data_y_transformed = lb.fit_transform(data_y)

accuracies = []

for i in range(30):
  data_train_x, data_test_x, data_train_y, data_test_y = train_test_split(data_x, data_y_transformed, test_size=0.5)

  model = Sequential()
  model.add(Dense(26, input_dim=(13)))
  model.add(Dense(3))
  model.add(Activation("softmax"))
  model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])
  model.fit(data_train_x, data_train_y, epochs=100, batch_size=1)

  loss, accuracy = model.evaluate(data_test_x, data_test_y)
  accuracies = np.append(accuracies, accuracy)

dev = accuracies.std()
med = np.average(accuracies)

print(f'Desvio Padrão = {dev}')
print(f'Média = {med}')