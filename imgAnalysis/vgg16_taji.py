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

# トレーニング用とバリデーション用の画像格納先
img_dir =  '/Users/corno/Python/imgAnalysis/img_category/'
train_dir = os.path.join(img_dir,'train/')
validation_dir = os.path.join(img_dir+'validation/')

result_dir = os.path.join(img_dir,'results/')
if not os.path.exists(result_dir):
    os.mkdir(result_dir)

# 分類するクラスをディレクトリから取得する
classes=os.listdir(train_dir)
classes.remove('.DS_Store') #除く
print(classes)
nb_classes = len(classes)

#画像の大きさ
img_rows = 150
img_cols = 125
channels = 3

batch_size = 50
nb_epoch = 30

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
    train_dir,
    target_size=(img_rows, img_cols),
    color_mode='rgb',
    classes=classes,
    class_mode='categorical',
    batch_size=batch_size,
    shuffle=True)

validation_generator = test_datagen.flow_from_directory(
    validation_dir,
    target_size=(img_rows, img_cols),
    color_mode='rgb',
    classes=classes,
    class_mode='categorical',
    batch_size=batch_size,
    shuffle=True)

history = model.fit_generator(
    train_generator,
    steps_per_epoch=train_generator.samples//batch_size,
    nb_epoch=nb_epoch,
    validation_data=validation_generator,
    # validation_steps=validation_generator.samples//batch_size
    validation_steps=4
)

history.history

# plot results
loss = history.history['loss']
val_loss = history.history['val_loss']

plt.plot(range(nb_epoch), loss, marker='.', label='loss')
plt.plot(range(nb_epoch), val_loss, marker='.', label='val_loss')
plt.legend(loc='best')
plt.grid()
plt.xlabel('epoch')
plt.ylabel('loss')
plt.show()

# plot results
acc = history.history['acc']
val_acc = history.history['val_acc']

plt.plot(range(nb_epoch), acc, marker='.', label='acc')
plt.plot(range(nb_epoch), val_acc, marker='.', label='val_acc')
plt.legend(loc='best')
plt.grid()
plt.xlabel('epoch')
plt.ylabel('acc')
plt.show()

import pickle

with open("%s/history1_taji.pkl"%result_dir, mode='wb') as f:
    pickle.dump(history.history, f)

model.save('%s/finetuning_taji.h5'%result_dir)

def save_history(history, result_file):
    loss = history.history['loss']
    acc = history.history['acc']
    val_loss = history.history['val_loss']
    val_acc = history.history['val_acc']
    nb_epoch = len(acc)

    with open(result_file, "w") as fp:
        fp.write("epoch\tloss\tacc\tval_loss\tval_acc\n")
        for i in range(nb_epoch):
            fp.write("%d\t%f\t%f\t%f\t%f\n" % (i, loss[i], acc[i], val_loss[i], val_acc[i]))

save_history(history, os.path.join(result_dir, 'history_taji.txt'))

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

predict('%s/%s21628662B_9_D_125.jpg'%(validation_dir,classes[0]))

get_ipython().magic('who')
get_ipython().magic('whos')

print("ok") # 確認
