import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

import os
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Convolution2D, MaxPooling2D
from keras.utils import np_utils
from keras.utils.vis_utils import plot_model
from keras.preprocessing.image import ImageDataGenerator

nb_epoch = 30

# トレーニング用とバリデーション用の画像格納先
img_dir =  '/Users/corno/Python/imgAnalysis/img_category/'
train_dir = os.path.join(img_dir,'train/')
validation_dir = os.path.join(img_dir+'validation/')

result_dir = os.path.join(img_dir,'results')
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

batch_size = 32
samples_per_epoch = 1190
nb_val_samples = 170

print("mainの上だよ")

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


if __name__ == '__main__':
    print("mainだよ")

    # CNNを構築
    model = Sequential()
    model.add(Convolution2D(32, 3, 3, input_shape=(img_rows, img_cols, channels)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Convolution2D(32, 3, 3))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Convolution2D(64, 3, 3))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Flatten())
    model.add(Dense(64))
    model.add(Activation('relu'))
    model.add(Dropout(0.5))
    model.add(Dense(nb_classes))
    model.add(Activation('softmax'))

    model.compile(loss='categorical_crossentropy',
                  optimizer='adam',
                  metrics=['accuracy'])

    # モデルのサマリを表示
    model.summary()
    plot_model(model, show_shapes=True, to_file=os.path.join(result_dir, 'model.png'))

    # ディレクトリの画像を使ったジェネレータ
    train_datagen = ImageDataGenerator(
        rescale=1.0 / 255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)

    test_datagen = ImageDataGenerator(rescale=1.0 / 255)

    train_generator = train_datagen.flow_from_directory(
        directory=train_dir,
        target_size=(img_rows, img_cols),
        color_mode='rgb',
        classes=classes,
        class_mode='categorical',
        batch_size=batch_size,
        shuffle=True)

    test_generator = test_datagen.flow_from_directory(
        directory=validation_dir,
        target_size=(img_rows, img_cols),
        color_mode='rgb',
        classes=classes,
        class_mode='categorical',
        batch_size=batch_size,
        shuffle=True)

    history = model.fit_generator(
        train_generator,
        samples_per_epoch=samples_per_epoch,
        nb_epoch=nb_epoch,
        validation_data=test_generator,
        nb_val_samples=nb_val_samples)

    save_history(history, os.path.join(result_dir, 'history_smallcnn.txt'))

    loss, acc = model.evaluate_generator(test_generator, val_samples=800)
    print('Test loss:', loss)
    print('Test acc:', acc)

print("mainの下だよ")
