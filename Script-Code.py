#install library untuk menghapus background 
pip install rembg[gpu,cli]

#masukkan library
from rembg import remove
from PIL import Image
import cv2

#masukkan kode deteksi tepi
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("apel.jpg")

edge = cv2.Canny(img,150,150)

plt.subplot(121), plt.imshow(img, cmap="gray")
plt.title("gambar asli"),plt.xticks([]),plt.yticks([])
plt.subplot(122),plt.imshow(edge,cmap="gray")
plt.title("gambar tepi"),plt.xticks([]),plt.yticks([])
plt.show()

#masukkan file foto yang ingin dihapus background nya
input_path = '/content/sample_data/pisang.jpg'
output_path = '/content/sample_data/pisang.png'

with open(input_path, 'rb') as i:
    with open(output_path, 'wb') as o:
        input = i.read()
        output = remove(input)
        o.write(output)

# input = Image.open(input_path)
# output = remove(input)
# output.save(output_path)