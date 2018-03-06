import os,re

IMG_DIR =  '/Users/corno/Python/imgAnalysis/img/'
TRAIN_DIR = os.path.join(IMG_DIR,'train/')
VAL_DIR = os.path.join(IMG_DIR+'validation/')

for item in os.listdir(TRAIN_DIR):
    if re.match('\.',item)!=None:
        continue
    itemNo = len(os.listdir(TRAIN_DIR+item))
    print("%s %d"%(item,itemNo))
print()

for item in os.listdir(VAL_DIR):
    if re.match('\.',item)!=None:
        continue
    itemNo = len(os.listdir(VAL_DIR+item))
    print("%s %d"%(item,itemNo))
