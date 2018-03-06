import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

import os
import requests # urlを読み込むためrequestsをインポート
from bs4 import BeautifulSoup # htmlを読み込むためBeautifulSoupをインポート

URL = "http://zozo.jp/men-category/jacket-outerwear/down-jacket/"
#list=URL.split("/") # /で文字列を分割
dirname=URL.split("/")[-2] #最後の文字列をファイルの名前にする
imgPath = 'imgAnalysis/scraping/'+dirname+"/"
if not os.path.exists(imgPath):
    os.mkdir(imgPath)

pages=1
images = [] # 画像リストの配列

for i in range(1,pages+1):
    if i==1:
        soup = BeautifulSoup(requests.get(URL).content,'lxml') # bsでURL内を解析
    else:
        soup = BeautifulSoup(requests.get(URL+"&pno=%d"%i).content,'lxml') # bsでURL内を解析

    for link in soup.find_all("img"): # imgタグを取得しlinkに格納
        if (link.get("data-src")!=None) and link.get("data-src").endswith(".jpg"): # imgタグ内の.jpgであるsrcタグを取得
            images.append(link.get("data-src")) # imagesリストに格納
            # print(link.get("data-src"))
            # elif link.get("src").endswith(".png"): # imgタグ内の.pngであるsrcタグを取得
            # images.append(link.get("src")) # imagesリストに格納


for target in images: # imagesからtargetに入れる
    re = requests.get(target)
    with open(imgPath + target.split('/')[-1], 'wb') as f: # imgフォルダに格納
        f.write(re.content) # .contentにて画像データとして書き込む

print("ok") # 確認
