#deteksi tepi
# memanggil library opencv
import cv2
import numpy as np
import matplotlib.pyplot as plt

# membuat variabel untuk memuat nilai gambar yang ada di folder kerja
image = cv2.imread("apel.jpg")
# fungsi untuk melakukan konversi dari BGR menjadi RGB.
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# digunakan untuk mendeteksi berbagai tepi pada gambar.
canny_output = cv2.Canny(image, 80, 80)

# berfungsi untuk menggambar banyak plot dalam satu gambar
plt.subplot(121), 
# untuk menampilkan image/citra BGR menjadi RGB
plt.imshow(cv2.cvtColor (image, cv2.COLOR_BGR2RGB))
#  digunakan untuk memberi judul pada plot.
plt.title("gambar asli"),plt.xticks([]),plt.yticks([])
# berfungsi untuk menggambar banyak plot dalam satu gambar
plt.subplot(122), 
# untuk menampilkan image/citra tepi pada gambar
plt.imshow(canny_output,cmap="gray")
#  digunakan untuk memberi judul pada plot.
plt.title("gambar tepi"),plt.xticks([]),plt.yticks([])
#menampilkan gambar
plt.show()
