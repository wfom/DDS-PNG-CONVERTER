import os
from PIL import Image

# Creating a list of dds files from those in the directory
dds_img = [f for f in os.listdir('.') if f.endswith('.dds')]

# Creating a folder to save png files
folder = 'PNG'
if not os.path.exists(folder):
    os.makedirs(folder)

# Convert and save each dds file in png format
for file in dds_img:
    img = Image.open(file)
    img.save(os.path.join(folder, os.path.splitext(file)[0] + '.png'))
    print(F"{file} --> png")

input("The files have been converted. Press [Enter] to close the program...")
