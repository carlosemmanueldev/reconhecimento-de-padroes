import cv2
import numpy as np
from google.colab.patches import cv2_imshow

# Carrega a imagem
img = cv2.imread('Fig1016(a)(building_original).png', cv2.IMREAD_GRAYSCALE)

# Suaviza a imagem
img = cv2.blur(img, (5, 5))

# Aplica o filtro de Sobel
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)

mag = np.sqrt(sobelx**2 + sobely**2)

# Aplica um limiar de 80 ao resultado da letra b
_, limiar = cv2.threshold(mag, 80, 255, cv2.THRESH_BINARY)

# Mostra a imagem
cv2_imshow(limiar)
cv2.waitKey(0)
cv2.destroyAllWindows()