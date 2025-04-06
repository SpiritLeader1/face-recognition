import os
import re
import pandas as pd
root = os.getcwd()
resim = []
for path, subdirs, files in os.walk(root):
    for name in files:
        if(re.search("png$",name)):
            resim.append(os.path.join(path, name))

            #print(os.path.join(path, name))

resim_dict = {"img_name":resim}
df = pd.DataFrame(resim_dict)
df.to_csv("studytask_old_img.csv",index=False) 