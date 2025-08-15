import cv2
import numpy as np
from google.colab.patches import cv2_imshow

# Carrega a imagem
img = cv2.imread('equacoes.png')

# Converte a imagem em escala de cinza
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Aplica um filtro de suavização
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Aplica thresholding adaptativo
thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 2)

# Aplica um filtro de abertura para remover imperfeições
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

# Inverte a imagem
result = cv2.bitwise_not(opening)

# Mostra a imagem
cv2_imshow(result)