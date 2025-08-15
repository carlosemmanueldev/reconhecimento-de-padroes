import pandas as pd
import numpy as np
from scipy.spatial import distance

data = pd.read_csv('iris.data.train', header=None,
                   names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])
data_test = pd.read_csv('iris.data.test', header=None,
                        names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])
true_data = pd.read_csv('iris.data.test', header=None,
                        names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])

sep_l_train = data['sepal_length'][0]
sep_w_train = data['sepal_width'][0]
pet_l_train = data['petal_length'][0]
pet_w_train = data['petal_width'][0]

train_one = np.array((sep_l_train, sep_w_train, pet_l_train, pet_w_train))

for i in range(len(data_test)):
    sep_l_test = data_test['sepal_length'][i]
    sep_w_test = data_test['sepal_width'][i]
    pet_l_test = data_test['petal_length'][i]
    pet_w_test = data_test['petal_width'][i]

    test = np.array((sep_l_test, sep_w_test, pet_l_test, pet_w_test))

    euclidean_distance = distance.euclidean(train_one, test)
    for j in range(1, len(data)):
        sep_l_train = data['sepal_length'][j]
        sep_w_train = data['sepal_width'][j]
        pet_l_train = data['petal_length'][j]
        pet_w_train = data['petal_width'][j]

        train = np.array((sep_l_train, sep_w_train, pet_l_train, pet_w_train))

        euclidean_distance_test = distance.euclidean(train, test)
        if euclidean_distance_test < euclidean_distance:
            data_test['class'][i] = data['class'][j]
            euclidean_distance = euclidean_distance_test

cont = 0
for i in range(len(true_data)):
    if true_data['class'][i] == data_test['class'][i]:
        cont += 1

print("Taxa de acerto: ", cont / len(true_data))