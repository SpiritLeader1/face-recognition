import os
import re
import pandas as pd
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
resim_dict = {"isSeen":isSeen,"Face_location":face_loc, "Intact_location":intact_loc,"Rearranged_location":rearrange_loc,"New_location":new_loc}
df = pd.DataFrame(resim_dict)
df.to_excel("data_img.xlsx",index=False)