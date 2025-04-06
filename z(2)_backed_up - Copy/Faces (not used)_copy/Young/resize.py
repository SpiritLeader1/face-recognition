import os
from PIL import Image
import re

target_width = 1024  # Change this to your desired width
target_height = 1280
# Load the image
root = os.getcwd()

for path, subdirs, files in os.walk(root):
    for name in files:
        if(bool(re.search("(png|jpeg|jpg)$",name))):
            image = Image.open(os.path.join(path,name))  # Replace with the path to your image file
# Set desired width and calculate the new height to maintain aspect ratio

# Resize the image
            resized_image = image.resize((target_width, target_height))

# Save or display the resized image
            resized_image.save(os.path.join(path,os.path.splitext(name)[0]+"_new"+os.path.splitext(name)[1]))  # Saves the resized image
            if((not bool(re.search("new",name)))):
                os.remove(os.path.join(path,name))