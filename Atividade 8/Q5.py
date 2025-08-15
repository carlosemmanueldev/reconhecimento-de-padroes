import numpy as np
from PIL import Image
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
images = []
images_neighbor = []
for train_index, test_index in sss.split(data, targets):
  images_split = []
  images_neighbor_split = []

  # Dividindo o conjunto de dados em treinamento e teste
  X_train, X_test = data[train_index], data[test_index]
  y_train, y_test = targets[train_index], targets[test_index]

  # Criando o 1-NN
  knn = KNeighborsClassifier(n_neighbors=1, weights="distance", metric="euclidean")

  # Treinando o classificador 1-NN
  knn.fit(X_train, y_train)

  # Fazendo a predição
  predicts = knn.predict(X_test)

  # Loop pelas classes previstas(predicts)
  for i, predict in enumerate(predicts):
    couple = []

    # Verificando se a classe é diferente da classe verdadeira
    if predict != y_test[i]:

      # Obtendo a imagem mais proxima no conjunto de treino
      neighbor = knn.kneighbors([X_test[i]], n_neighbors=1, return_distance=False)
      image_matrix = np.array_split(X_test[i], 112)
      neighbor_matrix = np.array_split(X_train[neighbor[0][0]], 112)
      couple.append(image_matrix)
      couple.append(neighbor_matrix)
    if couple:
      images_split.append(couple)
  images.append(images_split)

# Concatenando todas as imagens 
for i, images_split in enumerate(images):
  images1 = [np.concatenate(image, axis=1) for image in images_split]
  Image.fromarray(np.concatenate(np.array(images1))).save(f'/content/Q5_split_{i+1}.png')
  print(f'- Split {i+1}: OK!')