pip install rembg[gpu,cli]

from rembg import remove
from PIL import Image
import cv2

input_path = 'lemon.jpg'
output_path = 'lemon.png'

with open(input_path, 'rb') as i:
    with open(output_path, 'wb') as o:
        input = i.read()
        output = remove(input)
        o.write(output)

        