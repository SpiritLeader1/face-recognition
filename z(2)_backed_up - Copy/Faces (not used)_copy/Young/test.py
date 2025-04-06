import os
import re
import pandas as pd
root = os.getcwd()
isSeen = [False for i in range(48)]
print(len(isSeen))
face_loc= []
intact_loc = []
rearrange_loc = []
new_loc = []
placeholder = "pngtree-gray-network-placeholder-png-image_3416659_new.jpg"
for path, subdirs, files in os.walk(root):
    for name in files:
        if(bool(re.search("(png|jpeg|jpg)$",name)) and "pngtree" not in name):
            face_loc.append(os.path.join(path, name))
            intact_loc.append(os.path.join(root, placeholder))
            rearrange_loc.append(os.path.join(root,placeholder))
            new_loc.append(os.path.join(root, placeholder))
print(len(face_loc),len(intact_loc),len(rearrange_loc),len(new_loc))
resim_dict = {"isSeen":isSeen,"Face_location":face_loc, "Intact_location":intact_loc,"Rearranged_location":rearrange_loc,"New_location":new_loc}
df = pd.DataFrame(resim_dict)
df.to_excel("testtask_face_not_used_young.xlsx",index=False)