import os
import re #正規表現のモジュール
import shutil
import random

IN_DIR = '/Users/corno/Python/imgAnalysis/scraping/'
IMG_DIR =  '/Users/corno/Python/imgAnalysis/img_category/'
TRAIN_DIR = os.path.join(IMG_DIR,'train/')
VAL_DIR = os.path.join(IMG_DIR+'validation/')
#これが安全なpath joinの仕方なんやね〜->んなことなさそう。
# print(VAL_DIR)

# あるけどね。
if not os.path.exists(TRAIN_DIR):
    os.mkdir(TRAIN_DIR)
if not os.path.exists(VAL_DIR):
    os.mkdir(VAL_DIR)

# 元フォルダのディレクトリを取得する
for item in os.listdir(IN_DIR):
    if re.match('\.',item)!=None:
        # print(re.match('\.',item))
        continue
    # item_dir.append(re.findall(pattern,item)[-1])
    # print(re.findall(pattern,item)[-1])
    source = os.path.join(IN_DIR, item)
    dest = os.path.join(TRAIN_DIR, item)
    shutil.move(source, dest)
    print(os.path.join(TRAIN_DIR,item))
    for cood in os.listdir(os.path.join(TRAIN_DIR,item)):
        print(cood)
        if not os.path.exists(VAL_DIR+item+"/"):
            os.mkdir(VAL_DIR+item+"/")
        if random.random()<0.1:
            source = TRAIN_DIR+item+"/"+cood
            dest = VAL_DIR+item+"/"
            shutil.move(source, dest)
    # os.mkdir(os.path.join(TRAIN_DIR, re.findall(pattern,item)[-1]))
    # os.mkdir(os.path.join(VAL_DIR, re.findall(pattern,item)[-1]))

# print(len(item_dir))

# for item_name in item_dir:
#         source = os.path.join(IN_DIR, f)
#         dest = os.path.join(TRAIN_DIR, item_name)
#         shutil.copy(source, dest)


#数値だけ取り出してディレクトリ名にする
#数値にマッチするパターン（0～9の文字(数字)の繰り返し)を定義
# pattern=r'([+-]?[0-9]+\.?[0-9]*)'
# item_dir=[]


# # 訓練データの各ディレクトリからランダムに10枚をテストとする
# for d in os.listdir(TRAIN_DIR):
#     files = os.listdir(os.path.join(TRAIN_DIR, d))
#     random.shuffle(files)
#     for f in files[:10]:
#         source = os.path.join(TRAIN_DIR, d, f)
#         dest = os.path.join(VAL_DIR, d)
#         shutil.move(source, dest)
