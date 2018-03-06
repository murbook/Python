import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

import os
import requests # urlを読み込むためrequestsをインポート
from bs4 import BeautifulSoup # htmlを読み込むためBeautifulSoupをインポート
#変更だぞ〜
#さらに〜

#もいっちょ
URL = 'http://wear.jp/women-item/?brand_id=12230&type_category_id=108&'
imgdir=URL.split("/")[-1] #最後の文字列をファイルの名前にする
imgPath = '/Users/corno/Python/imgAnalysis/scraping/'+imgdir+"/"
if not os.path.exists(imgPath):
    os.mkdir(imgPath)

soup = BeautifulSoup(requests.get(URL).content,'lxml') # bsでURL内を解析
itemPageNo=1
# item一覧ページに対するwhile文。次ページがなくなったらbreak
while True:
    # 各itemに対してのfor文
    for link in soup.select('a[href^="/coordinate/?item_id="]'): # aタグを取得しlinkに格納
        itemUrl="http://wear.jp"+link.get("href")
        soup1 = BeautifulSoup(requests.get(itemUrl).content)
        # 次のページがある(coodinateが45以上)ならフォルダを作る
        if len(soup1.select("p.next > a"))!=0:
            itemdir=itemUrl.split("/")[-1] #最後の文字列をファイルの名前にする
            itemPath = imgPath+itemdir+"/"
            if not os.path.exists(itemPath):
                os.mkdir(itemPath)
            coodPageNo=1
            # coodinate一覧ページに対するwhile文。次ページがある限り続ける
            while True:
                # 各coodinateに対するfor文
                for link1 in soup1.find_all("img"):
                    if link1.get("width")=="232": # imgタグの属性widthが232であるとき画像を収集する
                        re = requests.get(link1.get("data-original"))
                        with open(itemPath+link1.get("data-original").split('/')[-1], 'wb') as f: # imgフォルダに格納
                            f.write(re.content) # .contentにて画像データとして書き込む
                if len(soup1.select("p.next > a"))==0:
                    break
                coodPageNo+=1
                soup1 = BeautifulSoup(requests.get("%s&pageno=%d"%(itemUrl,coodPageNo)).content,'lxml')
    print(itemPageNo)
    itemPageNo+=1
    soup = BeautifulSoup(requests.get("%spageno=%d"%(URL,itemPageNo)).content,'lxml')
print("ok") # 確認
