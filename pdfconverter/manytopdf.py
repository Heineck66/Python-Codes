import glob
import os

current_directory = os.getcwd()

images_list = glob.glob(f"{current_directory}\*")

from PIL import Image

for image_path in images_list:

    if image_path[:-3] == ".py":
        continue

    image_buffer = Image.open(image_path)
    image_converted = image_buffer.convert("RGB")
    image_converted.save(f"{image_path[:-3]}.pdf")
