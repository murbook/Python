import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

import os
from keras.applications.vgg16 import VGG16
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing import image
from keras.models import Sequential, Model
from keras.layers import Input, Activation, Flatten, Dense, Dropout
from keras import optimizers
import numpy as np
import matplotlib.pyplot as plt
from IPython.core.display import Image, display

batch_size = 32

classes = ['Women_T-shirt_ShortSleeves', 'Women_T-shirt_LongSleeves']
nb_classes = len(classes)

img_rows = 150
img_cols = 125
channels = 3

train_data_dir = '/Users/corno/Python/imgAnalysis/imgSleeves/train'
validation_data_dir = '/Users/corno/Python/imgAnalysis/imgSleeves/validation'

epochs = 50

result_dir = '/Users/corno/Python/imgAnalysis/imgSleeves/results'
if not os.path.exists(result_dir):
    os.mkdir(result_dir)


input_tensor = Input(shape=(img_rows, img_cols, channels))
base_model = VGG16(include_top=False, weights='imagenet', input_tensor=input_tensor)

base_model.summary()

x = base_model.output
x = Flatten(input_shape=base_model.output_shape[1:])(x)
x = Dense(256, activation='relu')(x)
x = Dropout(0.5)(x)
predictions = Dense(nb_classes, activation='softmax')(x)

model = Model(inputs=base_model.input, outputs=predictions)
model.summary()

model.layers[:15]

# 最後のconv層の直前までの層をfreeze
for layer in model.layers[:15]:
    layer.trainable = False

model.compile(loss='categorical_crossentropy',
              optimizer=optimizers.SGD(lr=1e-4, momentum=0.9),
              metrics=['accuracy'])

train_datagen = ImageDataGenerator(
    rescale=1.0 / 255,
    shear_range=0.2,# シアー変換
    zoom_range=0.2, #  ランダムにズーム
    rotation_range=5, # ランダムに回転する角度
    horizontal_flip=True # 水平方向に反転
)

test_datagen = ImageDataGenerator(rescale=1.0 / 255)

train_generator = train_datagen.flow_from_directory(
    train_data_dir,
    target_size=(img_rows, img_cols),
    color_mode='rgb',
    classes=classes,
    class_mode='categorical',
    batch_size=batch_size,
    shuffle=True)

validation_generator = test_datagen.flow_from_directory(
    validation_data_dir,
    target_size=(img_rows, img_cols),
    color_mode='rgb',
    classes=classes,
    class_mode='categorical',
    batch_size=batch_size,
    shuffle=True)

history = model.fit_generator(
    train_generator,
    steps_per_epoch=train_generator.samples//batch_size,
    epochs=epochs,
    validation_data=validation_generator,
    # validation_steps=validation_generator.samples//batch_size
    validation_steps=4
)

history.history

# plot results
loss = history.history['loss']
val_loss = history.history['val_loss']

plt.plot(range(epochs), loss, marker='.', label='loss')
plt.plot(range(epochs), val_loss, marker='.', label='val_loss')
plt.legend(loc='best')
plt.grid()
plt.xlabel('epoch')
plt.ylabel('loss')
plt.show()

# plot results
acc = history.history['acc']
val_acc = history.history['val_acc']

plt.plot(range(epochs), acc, marker='.', label='acc')
plt.plot(range(epochs), val_acc, marker='.', label='val_acc')
plt.legend(loc='best')
plt.grid()
plt.xlabel('epoch')
plt.ylabel('acc')
plt.show()

import pickle

with open("%s/history1.pkl"%result_dir, mode='wb') as f:
    pickle.dump(history.history, f)

model.save('%s/vgg16-finetuning.h5'%result_dir)

def predict(img_file_path):
    display(Image(img_file_path, width=150, unconfined=True))
    img = image.load_img(img_file_path, target_size=(img_rows, img_cols))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)

    # 学習時にImageDataGeneratorのrescaleで正規化したので同じ処理が必要！
    # これを忘れると結果がおかしくなるので注意
    x = x / 255.0

    # クラスを予測
    # 入力は1枚の画像なので[0]のみ
    pred = model.predict(x)[0]

    # 予測確率が高いトップ5を出力
    top = 5
    top_indices = pred.argsort()[-top:][::-1]
    result = [(classes[i], pred[i]) for i in top_indices]
    for x in result:
        print(x)

predict('%s/%s/21628662B_9_D_125.jpg'%(validation_data_dir,classes[0]))

get_ipython().magic('who')
get_ipython().magic('whos')

print("ok") # 確認
