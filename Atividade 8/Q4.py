import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import StratifiedShuffleSplit
from skimage.io import imread

# Carregando a base de dados ORL
data = []
targets = []
for i in range(1, 41):
    for j in range(1, 11):
        img = imread(f'/content/drive/MyDrive/orl/class_{str(i).rjust(2, "0")}/sample_{str(j).rjust(2, "0")}.png')
        data.append(img)
        targets.append(i)

data = np.array(data)
targets = np.array(targets)

# Convertendo as imagens em vetores de características
data = data.reshape(len(data), -1)

# Definindo o método de validação cruzada k-fold
sss = StratifiedShuffleSplit(test_size=.5, n_splits=10)

# Loop pelos folds
accuracies = []
for train_index, test_index in sss.split(data, targets):
    # Dividindo o conjunto de dados em treinamento e teste
    X_train, X_test = data[train_index], data[test_index]
    y_train, y_test = targets[train_index], targets[test_index]

    # Criando o 1-NN
    knn = KNeighborsClassifier(n_neighbors=1, weights="distance", metric="euclidean")

    # Treinando o classificador 1-NN
    knn.fit(X_train, y_train)

    # Calculando a acurácia
    accuracies.append(knn.score(X_test, y_test))

# Imprimindo a taxa de acerto
[print(f'Taxa de acerto (classe {i+1}): {acerto}') for i, acerto in enumerate(accuracies)]
print(f'Média de acertos total: {round(np.average(np.array(accuracies)), 2)}')