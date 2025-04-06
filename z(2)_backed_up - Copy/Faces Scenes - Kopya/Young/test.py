import os
import re
import pandas as pd
import random
root = os.getcwd()
isSeen = [True for i in range(48)]
print(len(isSeen))
face_loc= []
intact_loc = []
rearrange_loc = []
new_loc = []
for path, subdirs, files in os.walk(root):
    for name in files:
        if(bool(re.search("(png|jpeg|jpg)$",name)) and bool(re.search(r"\\(0_Face)\\",os.path.join(path, name)))):
            face_loc.append(os.path.join(path, name))
        if(bool(re.search("(png|jpeg|jpg)$",name)) and bool(re.search(r"\\(1_Intact)\\",os.path.join(path, name)))):
            intact_loc.append(os.path.join(path, name))
        if(bool(re.search("(png|jpeg|jpg)$",name)) and bool(re.search(r"\\(2_Rearranged)\\",os.path.join(path, name)))):
            rearrange_loc.append(os.path.join(path, name))
        if(bool(re.search("(png|jpeg|jpg)$",name)) and bool(re.search(r"\\(3_New)\\",os.path.join(path, name)))):
            new_loc.append(os.path.join(path, name))
print(len(face_loc),len(intact_loc),len(rearrange_loc),len(new_loc))
img_list = []
intactImageLocation = []
for i in range(len(face_loc)):
    list_element = [intact_loc[i], rearrange_loc[i], new_loc[i]]
    random.shuffle(list_element)
    intactImageLocation.append(list_element.index(intact_loc[i]) + 1)
    img_list.append(list_element)

print(len(img_list))
resim_dict = {"isSeen":isSeen,"Face_location":face_loc, "img1":[img_ele[0] for img_ele in img_list],"img2":[img_ele[1] for img_ele in img_list],"img3":[img_ele[2] for img_ele in img_list],"Intact Image Answer":intactImageLocation}
df = pd.DataFrame(resim_dict)
df.to_excel("testtask_face_used_young.xlsx",index=False)