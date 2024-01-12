import cv2
import numpy as np
import matplotlib.pyplot as plt

# Fungsi untuk melakukan deteksi tepi pada gambar
def edge_detection(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150)
    return cv2.cvtColor(edges, cv2.COLOR_GRAY2RGB)

# Fungsi untuk melakukan segmentasi (hapus background) pada gambar
def remove_background(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower_red = np.array([0, 0, 0])  # ambang batas bawah untuk warna merah 
    upper_red = np.array([10, 400, 255])  # ambang batas atas untuk warna merah 
    mask = cv2.inRange(hsv, lower_red, upper_red)
    result = cv2.bitwise_and(image, image, mask=mask)
    return result

# Baca gambar original
original = cv2.imread('Wajib/apel2.jpg')

# Deteksi tepi pada gambar
edges = edge_detection(original)

# Hapus background pada gambar dengan segmentasi warna merah
segmented = remove_background(original)

# Tampilkan ketiga gambar
plt.figure(figsize=(10, 5))

# Gambar original
plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(original, cv2.COLOR_BGR2RGB))
plt.title('Gambar original')
plt.axis('off')

# Gambar dengan deteksi tepi
plt.subplot(1, 3, 2)
plt.imshow(edges)
plt.title('Deteksi Tepi Gambar')
plt.axis('off')

# Gambar dengan segmentasi 
plt.subplot(1, 3, 3)
plt.imshow(cv2.cvtColor(segmented, cv2.COLOR_BGR2RGB))
plt.title('Segmentasi')
plt.axis('off')

# Tampilkan jendela
plt.show()