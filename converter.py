import os
from PIL import Image

source_folder = 'assets'

output_folder = 'assets_png'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(source_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff', '.webp')):
        # Получаем путь к файлу
        file_path = os.path.join(source_folder, filename)
        # Загружаем изображение
        image = Image.open(file_path)
        # Конвертируем в PNG
        filename_without_extension = os.path.splitext(filename)[0]
        output_file_path = os.path.join(output_folder, f'{filename_without_extension}.png')
        image.save(output_file_path, 'PNG')
        print(f'Изображение {filename} конвертировано в {output_file_path}')

print('Все изображения конвертированы.')
