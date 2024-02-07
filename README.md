# Cropper

Converts portraits to PNG format and crops them using a circular mask.

**Requirements:**

- Python 3

First, you need to install these libraries (if you haven't already):

    pip3 install opencv-python-headless pillow

**Application steps:**

1. Place the photo in the _assets_ folder if you need to convert portraits to PNG. Create a folder named _assets_png_ and put portraits in it if they are already in PNG format.

2. If the portraits need to be converted to PNG, run the command: `python3 converter.py`. If conversion is not necessary, proceed to step 3.

3. After ensuring that all portraits have been converted to PNG and are located in the _assets_png_ folder, run the command: `python3 main.py`.

The converted photos will be stored in the cropped_images folder.
