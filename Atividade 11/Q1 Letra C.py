import cv2
from matplotlib import pyplot as plt
from google.colab.patches import cv2_imshow

# Imagem Fig0320(1)(top_left)
img1 = cv2.imread('Fig0320(1)(top_left).png', cv2.IMREAD_GRAYSCALE)

equ1 = cv2.equalizeHist(img1)
hist1 = cv2.calcHist([equ1], [0], None, [256], [0, 256])

plt.plot(hist1)
plt.title('Histograma Equalizado - Fig0320(1)(top_left).png')
plt.xlabel('Intensidade de pixel')
plt.ylabel('Número de pixels')
plt.show()

# Imagem Fig0320(2)(2nd_from_top)
img2 = cv2.imread('Fig0320(2)(2nd_from_top).png', cv2.IMREAD_GRAYSCALE)

equ2 = cv2.equalizeHist(img2)
hist2 = cv2.calcHist([equ2], [0], None, [256], [0, 256])

plt.plot(hist2)
plt.title('Histograma Equalizado - Fig0320(2)(2nd_from_top).png')
plt.xlabel('Intensidade de pixel')
plt.ylabel('Número de pixels')
plt.show()

# Imagem Fig0320(3)(third_from_top)
img3 = cv2.imread('Fig0320(3)(third_from_top).png', cv2.IMREAD_GRAYSCALE)

equ3 = cv2.equalizeHist(img3)
hist3 = cv2.calcHist([equ3], [0], None, [256], [0, 256])

plt.plot(hist3)
plt.title('Histograma Equalizado - Fig0320(3)(third_from_top).png')
plt.xlabel('Intensidade de pixel')
plt.ylabel('Número de pixels')
plt.show()

# Imagem Fig0320(4)(bottom_left)
img4 = cv2.imread('Fig0320(4)(bottom_left).png', cv2.IMREAD_GRAYSCALE)

equ4 = cv2.equalizeHist(img4)
hist4 = cv2.calcHist([equ4], [0], None, [256], [0, 256])

plt.plot(hist4)
plt.title('Histograma Equalizado - Fig0320(4)(bottom_left).png')
plt.xlabel('Intensidade de pixel')
plt.ylabel('Número de pixels')
plt.show()

# Imagem Fig0323(a)(mars_moon_phobos)
img5 = cv2.imread('Fig0323(a)(mars_moon_phobos).png', cv2.IMREAD_GRAYSCALE)

equ5 = cv2.equalizeHist(img5)
hist5 = cv2.calcHist([equ5], [0], None, [256], [0, 256])

plt.plot(hist5)
plt.title('Histograma Equalizado - Fig0323(a)(mars_moon_phobos).png')
plt.xlabel('Intensidade de pixel')
plt.ylabel('Número de pixels')
plt.show()

# Imagem Fig0309(a)(washed_out_aerial_image)
img6 = cv2.imread('Fig0309(a)(washed_out_aerial_image).png', cv2.IMREAD_GRAYSCALE)

equ6 = cv2.equalizeHist(img6)
hist6 = cv2.calcHist([equ6], [0], None, [256], [0, 256])

plt.plot(hist6)
plt.title('Histograma Equalizado - Fig0309(a)(washed_out_aerial_image).png')
plt.xlabel('Intensidade de pixel')
plt.ylabel('Número de pixels')
plt.show()

# Imagem Fig0308(a)(fractured_spine)
img7 = cv2.imread('Fig0308(a)(fractured_spine).png', cv2.IMREAD_GRAYSCALE)

equ7 = cv2.equalizeHist(img7)
hist7 = cv2.calcHist([equ7], [0], None, [256], [0, 256])

plt.plot(hist7)
plt.title('Histograma Equalizado - Fig0308(a)(fractured_spine).png')
plt.xlabel('Intensidade de pixel')
plt.ylabel('Número de pixels')
plt.show()