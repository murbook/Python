import sys
sys.path.append('/Users/corno/.pyenv/versions/anaconda3-4.4.0/lib/python3.6/site-packages')

from keras.applications.vgg16 import VGG16, preprocess_input, decode_predictions
from keras.preprocessing import image
import numpy as np
from PIL import Image

vgg16 = VGG16(weights='imagenet')
imgPath="imgAnalysis/img/bc4fb9389af0818cd9ef94450730992d--ten-commandments-funny-cats.jpg"


def predict(img_file_path):
    im = Image.open(imgPath)
    im.show()
    img = image.load_img(img_file_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)

    preds = vgg16.predict(preprocess_input(x))

    # 予測確率が高いトップ5を出力
    top = 5
    results = decode_predictions(preds, top=top)[0]
    for result in results:
        print(result)

predict(imgPath)
