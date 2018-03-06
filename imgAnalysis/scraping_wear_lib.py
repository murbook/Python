import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

import os
import urllib.request # urlを読み込むためurllib.requestをインポート
from bs4 import BeautifulSoup # htmlを読み込むためBeautifulSoupをインポート

URL = 'http://wear.jp/men-item/?brand_id=12230&type_category_id=101&category_id=2001'
#list=URL.split("/") # /で文字列を分割
dirname=URL.split("/")[-1] #最後の文字列をファイルの名前にする
imgPath = 'scraping/'+dirname+"/"
if not os.path.exists(imgPath):
    os.mkdir(imgPath)

pages=5
images = [] # 画像リストの配列

ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) '\
     'AppleWebKit/537.36 (KHTML, like Gecko) '\
     'Chrome/55.0.2883.95 Safari/537.36 '
req = urllib.request.Request(URL, headers={'User-Agent': ua})
html = urllib.request.urlopen(req)

for i in range(1,pages+1):
    print("a")
    if i==1:
        soup = BeautifulSoup(html, "html.parser")
        # soup = BeautifulSoup(urllib.urlopen(url).read()) # bsでURL内を解析
        print("b")
    else:
        soup = BeautifulSoup(html, "html.parser")
        # soup = BeautifulSoup(urllib.urlopen(url).read()) # bsでURL内を解析
        print("c")
    for link in soup.find_all("img"): # imgタグを取得しlinkに格納
        print("d")
        if (link.get("data-original")!=None) and link.get("data-original").endswith(".jpg"): # imgタグ内の.jpgであるsrcタグを取得
            images.append(link.get("data-original")) # imagesリストに格納
            print(link.get("data-original"))
        # elif link.get("src").endswith(".png"): # imgタグ内の.pngであるsrcタグを取得
        # images.append(link.get("src")) # imagesリストに格納


for target in images: # imagesからtargetに入れる
    re = urllib.request.urlopen(target)
    with open(imgPath + target.split('/')[-1], 'wb') as f: # imgフォルダに格納
        f.write(re.content) # .contentにて画像データとして書き込む

print("ok") # 確認
