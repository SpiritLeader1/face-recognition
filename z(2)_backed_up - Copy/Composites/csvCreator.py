import os
import re
import pandas as pd

# Set root to the relative path from the script's location
root = os.path.join(os.path.dirname(__file__), "..")

youngKeys = r".*Young.*\.png$"
oldKeys = r".*Old.*\.png$"
resim = []

for path, subdirs, files in os.walk(root):
    for name in files:
        if re.search(oldKeys, name, re.IGNORECASE):
            resim.append(os.path.join(path, name))
            print(os.path.join(path, name))

resim_dict = {"img_name": resim}
df = pd.DataFrame(resim_dict)
df.to_csv("data_img.csv", index=False)