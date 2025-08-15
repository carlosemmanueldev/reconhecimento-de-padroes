import numpy as np
from sklearn.datasets import load_iris

# Função de ativação do neurônio, que no caso será a função degrau
def step(x):
    return np.where(x >= 0, 1, 0)


class Neuron:
    def __init__(self, input_size):
        self.w = np.random.rand(input_size)
        self.b = np.random.rand()

    def forward(self, x):
        z = np.dot(x, self.w) + self.b
        a = step(z)
        return a

    def backward(self, x, y, a, lr):
        d = y - a
        dw = lr * d * x
        db = lr * d
        self.w += dw
        self.b += db


def train_and_test_neuron(X_train, y_train, X_test, y_test, lr, epochs=100):
    model = Neuron(input_size=X_train.shape[1])

    for epoch in range(epochs):
        for x, y in zip(X_train, y_train):
            a = model.forward(x)
            model.backward(x, y, a, lr)

    predictions = []
    for x in X_test:
        a = model.forward(x)
        predictions.append(a)

    predictions = np.array(predictions)

    error = np.mean(predictions != y_test)

    return error

#Definindo para letra A
iris = load_iris()
X = iris.data
y = iris.target

# Define a Iris-setosa = 1, demais = 0
y[y != 0] = -1
y[y == 0] = 1
y[y != 1] = 0

X_train = np.concatenate((X[:25, :], X[50:75, :], X[100:125, :]))
y_train = np.concatenate((y[:25], y[50:75], y[100:125]))

X_test = np.concatenate((X[25:50, :], X[75:100, :], X[125:150, :]))
y_test = np.concatenate((y[25:50], y[75:100], y[125:150]))

# Normalização dos dados para que tenham média zero e variância unitária
X_train = (X_train - np.mean(X_train, axis=0)) / np.std(X_train, axis=0)
X_test = (X_test - np.mean(X_test, axis=0)) / np.std(X_test, axis=0)

lrs = [0.1, 1.0, 10.0]
n_repetitions = 30
n_epochs = 100

for lr in lrs:
    errors = []
    for i in range(n_repetitions):
        error = train_and_test_neuron(X_train, y_train, X_test, y_test, lr, epochs=n_epochs)
        errors.append(error)

    mean_error = np.mean(errors)
    std_error = np.std(errors)

    print('LETRA A')
    print('Taxa de aprendizagem:', lr)
    print('Erro médio:', mean_error)
    print('Desvio padrão do erro:', std_error)
    print('\n')


#Definindo para letra B
iris = load_iris()
X = iris.data
y = iris.target

# Define a Iris-virgínica = 1, demais = 0
y[y != 2] = -1
y[y == 2] = 1
y[y != 1] = 0

X_train = np.concatenate((X[:25, :], X[50:75, :], X[100:125, :]))
y_train = np.concatenate((y[:25], y[50:75], y[100:125]))

X_test = np.concatenate((X[25:50, :], X[75:100, :], X[125:150, :]))
y_test = np.concatenate((y[25:50], y[75:100], y[125:150]))

# Normalização dos dados para que tenham média zero e variância unitária
X_train = (X_train - np.mean(X_train, axis=0)) / np.std(X_train, axis=0)
X_test = (X_test - np.mean(X_test, axis=0)) / np.std(X_test, axis=0)

lrs = [0.1, 1.0, 10.0]
n_repetitions = 30
n_epochs = 100

for lr in lrs:
    errors = []
    for i in range(n_repetitions):
        error = train_and_test_neuron(X_train, y_train, X_test, y_test, lr, epochs=n_epochs)
        errors.append(error)

    mean_error = np.mean(errors)
    std_error = np.std(errors)

    print('LETRA B')
    print('Taxa de aprendizagem:', lr)
    print('Erro médio:', mean_error)
    print('Desvio padrão do erro:', std_error)
    print('\n')