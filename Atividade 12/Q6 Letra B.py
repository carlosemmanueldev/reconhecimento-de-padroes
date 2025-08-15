import cv2
import numpy as np
from google.colab.patches import cv2_imshow

# Carrega a imagem
img = cv2.imread('Fig1016(a)(building_original).png', cv2.IMREAD_GRAYSCALE)

# Suaviza a imagem
img = cv2.blur(img, (5, 5))
cv2_imshow(img)

# Aplica o filtro de Sobel
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)

mag = np.sqrt(sobelx**2 + sobely**2)

# Mostra a imagem
cv2_imshow(mag)
cv2.waitKey(0)
cv2.destroyAllWindows()