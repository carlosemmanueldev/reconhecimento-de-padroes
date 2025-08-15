import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

cols = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']

data = pd.read_csv('iris.data', header=None, names=cols)

data_x = data[cols[:-1]]
data_y = data['class']

kmeans = KMeans(n_clusters=5, max_iter=10, init='k-means++')

# Executa o algoritmo de k-médias para 10 iterações
n_iterations = 10
distances = np.zeros((n_iterations, data_x.shape[0]))

for i in range(n_iterations):
    # Executa o algoritmo de k-médias com o número máximo de iterações e centróides iniciais da iteração anterior
    kmeans.fit(data_x)

    # Calcula a distância de cada exemplo ao centróide mais próximo
    distances[i] = np.min(kmeans.transform(data_x), axis=1)

# Calcula a média e o desvio padrão das distâncias em cada iteração
mean_distances = np.mean(distances, axis=1)
std_distances = np.std(distances, axis=1)

# Imprime a tabela com as médias e desvios padrão
print('Iteração\tMédia\tDesvio padrão')
for i in range(n_iterations):
    print('{}\t\t{:.4f}\t{:.4f}'.format(i+1, mean_distances[i], std_distances[i]))