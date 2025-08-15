import cv2
from google.colab.patches import cv2_imshow
import numpy as np

img = cv2.imread('LUA.png')

cv2_imshow(img)

# mascara
mascara = np.array([[-1, -1, -1],
                   [-1, 8, -1],
                   [-1, -1, -1]])

LaplacianImage = cv2.filter2D(src=img, 
                              ddepth=-1, 
                              kernel=mascara)


c = 1
g = img + c*LaplacianImage

gClip = np.clip(g, 0, 255)

cv2_imshow(gClip)