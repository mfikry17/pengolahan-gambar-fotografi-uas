import cv2 # pernyataan Python yang digunakan untuk mengimpor modul OpenCV
import numpy as np # pernyataan Python yang digunakan untuk mengimpor modul NumPy 

# Untuk Membaca citra
nama_file_citra = 'Fotografi\cat3.jpg'  # Untuk nama file citra
citra = cv2.imread(nama_file_citra) # Digunakan untuk membaca citra dari file

# Untuk Deteksi tepi menggunakan metode Canny
tepi = cv2.Canny(citra, 50, 200)

# Untuk Mengonversi citra ke dalam format HSV
citra_hsv = cv2.cvtColor(citra, cv2.COLOR_BGR2HSV)

# Untuk Menentukan rentang warna latar belakang yang ingin dihapus
lower_latar_belakang = np.array([0, 0, 100]) # Sesuaikan dengan gambar 
upper_latar_belakang = np.array([300, 60, 300]) #Sesuaikan dengan gambar

# Untuk Membuat mask untuk warna latar belakang
mask_latar_belakang = cv2.inRange(citra_hsv, lower_latar_belakang, upper_latar_belakang)

# Untuk Mengganti piksel latar belakang dengan warna hitam
citra_tanpa_latar = cv2.bitwise_and(citra, citra, mask=~mask_latar_belakang)

# Untuk Menampilkan citra asli, citra deteksi tepi, dan citra tanpa latar belakang
cv2.imshow('Citra Asli', citra)
cv2.imshow('Deteksi Tepi', tepi)
cv2.imshow('Tanpa Latar Belakang', citra_tanpa_latar)
cv2.waitKey(0)
cv2.destroyAllWindows()
# cv2.waitKey dan cv2.destroyAllWindows Digunakan untuk menunggu penekanan tombol dan menutup jendela setelah selesai.
 