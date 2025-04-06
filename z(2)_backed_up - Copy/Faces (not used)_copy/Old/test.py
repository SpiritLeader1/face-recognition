import os
import re
import pandas as pd
import random
root = os.getcwd()
isSeen = [False for i in range(48)]
print(len(isSeen))
face_loc= []
intact_loc = []
rearrange_loc = []
new_loc = []
intactImageLocation = []
x = [1, 2, 3]
placeholder = "pngtree-gray-network-placeholder-png-image_3416659_new.jpg"
for path, subdirs, files in os.walk(root):
    for name in files:
        if(bool(re.search("(png|jpeg|jpg)$",name)) and "pngtree" not in name):
            face_loc.append(os.path.join(path, name))
            intact_loc.append(os.path.join(root, placeholder))
            rearrange_loc.append(os.path.join(root,placeholder))
            new_loc.append(os.path.join(root, placeholder))
            intactImageLocation.append(random.choice(x))
print(len(face_loc),len(intact_loc),len(rearrange_loc),len(new_loc))
resim_dict = {"isSeen":isSeen,"Face_location":face_loc, "img1":intact_loc,"img2":rearrange_loc,"img3":new_loc,"intactImageLocation": intactImageLocation}
df = pd.DataFrame(resim_dict)
df.to_excel("testtask_face_not_used_old.xlsx",index=False)