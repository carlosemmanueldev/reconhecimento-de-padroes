import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn_extra.cluster import KMedoids
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report

iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.5, stratify=iris.target, random_state=42)

k = 9
kmedoids = KMedoids(n_clusters=k, random_state=42)
kmedoids.fit(X_train)

centroids = kmedoids.cluster_centers_
distances = np.sqrt(((X_train - centroids[:, np.newaxis])**2).sum(axis=2))
closest_points = np.argmin(distances, axis=1)
X_train_reduced = X_train[np.isin(np.arange(len(X_train)), closest_points)]
y_train_reduced = y_train[np.isin(np.arange(len(X_train)), closest_points)]

knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train_reduced, y_train_reduced)

y_pred = knn.predict(X_test)
print(classification_report(y_test, y_pred, target_names=['setosa', 'versicolor', 'virginica']))