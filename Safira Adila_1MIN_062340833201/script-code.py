#install library untuk menghapus background (sagmentasi citra)
pip install rembg[gpu,cli]

#masukkan library
from rembg import remove
from PIL import Image
import cv2

#masukkan file foto yang ingin dihapus background nya
input_path = '/content/sample_data/pisang.jpg'
output_path = '/content/sample_data/pisang.png'

with open(input_path, 'rb') as i:
    with open(output_path, 'wb') as o:
        input = i.read()
        output = remove(input)
        o.write(output)

#masukkan kode untuk mengubah gambar asli menjadi citra deteksi tepi
import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("apel.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

canny_output = cv2.Canny(image, 80, 80)

plt.subplot(121), plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
plt.title("gambar asli"),plt.xticks([]),plt.yticks([])
plt.subplot(122), plt.imshow(canny_output,cmap="gray")
plt.title("citra deteksi tepi"),plt.xticks([]),plt.yticks([])
plt.show()