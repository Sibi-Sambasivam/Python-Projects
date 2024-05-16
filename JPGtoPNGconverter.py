import sys
import os
from PIL import Image

image_folder = sys.argv[1]
output_folder = sys.argv[2]

if not os.path.exists(output_folder):
	os.makedirs(output_folder)

for filename in os.listdir(image_folder):
    input_path = os.path.join(image_folder, filename) 
    img = Image.open(input_path)
    clean_name = os.path.splitext(filename)[0]
    output_path = os.path.join(output_folder, f'{clean_name}.png')
    img.save(output_path, 'PNG')
    print('All done!') 



