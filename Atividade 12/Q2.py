import cv2
import numpy as np
import matplotlib.pyplot as plt
from google.colab.patches import cv2_imshow

# Carregando a imagem
img = cv2.imread('Fig0340(a)(dipxe_text).png')

# Separando os canais de cor
b, g, r = cv2.split(img)

# Filtro gaussiano em cada canal de cor
ksize = (5, 5)
sigma = 3
b_blur = cv2.GaussianBlur(b, ksize, sigma)
g_blur = cv2.GaussianBlur(g, ksize, sigma)
r_blur = cv2.GaussianBlur(r, ksize, sigma)

# Máscaras de realce em cada canal de cor
k = 2
b_mask = cv2.addWeighted(b, k, b_blur, -k + 1, 0)
g_mask = cv2.addWeighted(g, k, g_blur, -k + 1, 0)
r_mask = cv2.addWeighted(r, k, r_blur, -k + 1, 0)

# Unindo os canais de cor novamente
img_masked = cv2.merge((b_mask, g_mask, r_mask))

# Exibindo a imagem resultante
cv2_imshow(img_masked)