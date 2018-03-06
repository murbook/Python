# 環境を統合したからもう要らない
# import sys
# sys.path.append('/Users/corno/.pyenv/versions/anaconda3-4.4.0/lib/python3.6/site-packages')

from PIL import Image

#イメージのパス
imgPath="imgAnalysis/img/bc4fb9389af0818cd9ef94450730992d--ten-commandments-funny-cats.jpg"
#画像の読み込み
im = Image.open(imgPath)
#表示
im.show()
