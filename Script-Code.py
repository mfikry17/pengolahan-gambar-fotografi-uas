#install library untuk menghapus background 
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

# input = Image.open(input_path)
# output = remove(input)
# output.save(output_path)