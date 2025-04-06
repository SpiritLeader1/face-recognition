import os
import pandas as pd
import re
import random
root = os.getcwd()
logicList = list()
logicList.extend([True for i in range(0,50)])
logicList.extend([False for i in range(0,50)])
imageNames = [root+"\\"+name for name in os.listdir() if re.search("jpeg$",name)]
imgName1 = list()
imgName2 = list()
i = 0
for logic in logicList:
    if logic:
        imgName1.append(imageNames[i])
        imgName2.append(imageNames[i])
    else:
        imageNumbers = list(range(50,101))
        imgName1.append(imageNames[i])
        imageNumbers.remove(i)
        imgName2.append(imageNames[random.choice(imageNumbers)])
    i += 1 

dictData = {"LogicList":logicList, "imgName1":imgName1, "imgName2":imgName2}
df = pd.DataFrame(dictData)
df.to_excel("interval_test.xlsx", index=False)





