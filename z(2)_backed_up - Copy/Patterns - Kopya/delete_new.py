import os
import re

# Load the image
root = os.getcwd()

for path, subdirs, files in os.walk(root):
    for name in files:
        if(bool(re.search("(png|jpeg|jpg)$",name))):
          
            if((bool(re.search("(png|jpeg|jpg)$",name)) and bool(re.search("new_new",name)))):
                os.remove(os.path.join(path,name))
