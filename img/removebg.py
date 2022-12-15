from rembg import remove
from PIL import Image
input_path='cl.jpg'
out_path='output.png'
input=Image.open(cl.jpg)
output=remove(input)
output.save(out_path)