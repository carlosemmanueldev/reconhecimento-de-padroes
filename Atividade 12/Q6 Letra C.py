import cv2
import numpy as np
from google.colab.patches import cv2_imshow

# Carrega a imagem
img = cv2.imread('Fig1016(a)(building_original).png')

# Aplica o filtro de Sobel
sobelx = cv2.Sobel(img, cv2.CV_8U, 1, 0, ksize=3)
sobely = cv2.Sobel(img, cv2.CV_8U, 0, 1, ksize=3)

absx = cv2.convertScaleAbs(sobelx)
absy = cv2.convertScaleAbs(sobely)

sobel_edge = cv2.addWeighted(absx, 0.5, absy, 0.5, 0)

# Aplica um limiar de 80 ao resultado da letra a
_, limiar = cv2.threshold(sobel_edge, 80, 255, cv2.THRESH_BINARY)

# Mostra a imagem
cv2_imshow(limiar)
cv2.waitKey(0)
cv2.destroyAllWindows()