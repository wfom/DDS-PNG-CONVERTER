import os
from PIL import Image

# Создаем список dds-файлов
dds_files = [f for f in os.listdir('.') if f.endswith('.dds')]

# Создаем папку для сохранения png-файлов
save_folder = 'PNG'
if not os.path.exists(save_folder):
    os.makedirs(save_folder)

# Конвертируем и сохраняем каждый dds-файл
for file in dds_files:
    img = Image.open(file)
    img.save(os.path.join(save_folder, os.path.splitext(file)[0] + '.png'))
