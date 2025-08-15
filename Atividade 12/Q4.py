import cv2
import numpy as np
import matplotlib.pyplot as plt
from google.colab.patches import cv2_imshow

def plot_image(images, title):
    n=131
    plt.figure(figsize=(15,15))
    c=0
    for img in images:
        plt.subplot(n)
        plt.title(title[c])
        plt.imshow(img,interpolation = 'nearest', cmap = plt.cm.gray)
        plt.axis('off')
        n+=1
        c+=1
    plt.show()

# leitura da imagem
img = cv2.imread('Fig1007(a)(wirebond_mask).png', cv2.COLOR_BGR2GRAY)

# mascaras
mascara_horizontal = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
mascara_vertical = np.array([[-1,0, 1], [-2, 0, 2], [-1, 0, 1]])
mascara_45 = np.array([[0, 1, 2], [-1, 0, 1], [-2, -1, 0]])
mascara_135 = np.array([[-2, -1, 0], [-1, 0, 1], [0, 1, 2]])
mascara_30 = np.array([[1, 1, 1, 1, 0], [1, 1, 0, 0, 0], [0, 0, 0, -1, -1], [0, -1, -1, -1, -1]])

img_horizontal = cv2.filter2D(img, -1, mascara_horizontal)
img_vertical = cv2.filter2D(img, -1, mascara_vertical)
img_45 = cv2.filter2D(img, -1, mascara_45)
img_135 = cv2.filter2D(img, -1, mascara_135)
img_30 = cv2.filter2D(img, -1, mascara_30)

plot_image([img, img_horizontal, img_vertical], ['original', 'horizontal', 'vertical'])
plot_image([img_45, img_135, img_30], ['45°', '135°', '30°'])