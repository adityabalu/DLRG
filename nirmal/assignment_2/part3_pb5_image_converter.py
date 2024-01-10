import sys
from PIL import Image

# check if an image filename is provided as an argument
if len(sys.argv) < 2:
    print("Usage: python part3_pb5_image_converter.py image_filename")
    sys.exit()

# open the image file
image_filename = sys.argv[1]
try:
    image = Image.open(image_filename)
except IOError:
    print("Error: Unable to open image file")
    sys.exit()

# resize the image to 224x224
image = image.resize((224, 224))

# convert the image to JPEG format
if image.format != "JPEG":
    image = image.convert("RGB")
    new_image_filename = image_filename.split('.')[0] + "_resized.jpg"
    image.save(new_image_filename, "JPEG")
    print(f"{image_filename} has been converted to {new_image_filename}")
else:
    print(f"{image_filename} is already in JPEG format")
    image.save(new_image_filename, "JPEG")
    
