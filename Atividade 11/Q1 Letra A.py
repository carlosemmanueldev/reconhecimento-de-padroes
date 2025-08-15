import cv2
from matplotlib import pyplot as plt

# Imagem Fig0320(1)(top_left)
img1 = cv2.imread('Fig0320(1)(top_left).png', cv2.IMREAD_GRAYSCALE)

hist1 = cv2.calcHist([img1],[0],None,[256],[0,256])

plt.hist(img1.ravel(),256,[0,256])
plt.title('Histograma - Fig0320(1)(top_left).png')
plt.show()

# Imagem Fig0320(2)(2nd_from_top)
img2 = cv2.imread('Fig0320(2)(2nd_from_top).png', cv2.IMREAD_GRAYSCALE)

hist2 = cv2.calcHist([img2],[0],None,[256],[0,256])

plt.hist(img2.ravel(),256,[0,256])
plt.title('Histograma - Fig0320(2)(2nd_from_top).png')
plt.show()

# Imagem Fig0320(3)(third_from_top)
img3 = cv2.imread('Fig0320(3)(third_from_top).png', cv2.IMREAD_GRAYSCALE)

hist3 = cv2.calcHist([img3],[0],None,[256],[0,256])

plt.hist(img3.ravel(),256,[0,256])
plt.title('Histograma - Fig0320(3)(third_from_top).png')
plt.show()

# Imagem Fig0320(4)(bottom_left)
img4 = cv2.imread('Fig0320(4)(bottom_left).png', cv2.IMREAD_GRAYSCALE)

hist4 = cv2.calcHist([img4],[0],None,[256],[0,256])

plt.hist(img4.ravel(),256,[0,256])
plt.title('Histograma - Fig0320(4)(bottom_left).png')
plt.show()

# Imagem Fig0323(a)(mars_moon_phobos)
img5 = cv2.imread('Fig0323(a)(mars_moon_phobos).png', cv2.IMREAD_GRAYSCALE)

hist5 = cv2.calcHist([img5],[0],None,[256],[0,256])

plt.hist(img5.ravel(),256,[0,256])
plt.title('Histograma - Fig0323(a)(mars_moon_phobos).png')
plt.show()

# Imagem Fig0309(a)(washed_out_aerial_image)
img6 = cv2.imread('Fig0309(a)(washed_out_aerial_image).png', cv2.IMREAD_GRAYSCALE)

hist6 = cv2.calcHist([img6],[0],None,[256],[0,256])

plt.hist(img6.ravel(),256,[0,256])
plt.title('Histograma - Fig0309(a)(washed_out_aerial_image).png')
plt.show()

# Imagem Fig0308(a)(fractured_spine)
img7 = cv2.imread('Fig0308(a)(fractured_spine).png', cv2.IMREAD_GRAYSCALE)

hist7 = cv2.calcHist([img7],[0],None,[256],[0,256])

plt.hist(img7.ravel(),256,[0,256])
plt.title('Histograma - Fig0308(a)(fractured_spine).png')
plt.show()