from keras.applications.vgg16 import VGG16
from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten, Dropout
from keras.layers import Dense, Dropout,ZeroPadding2D
from keras.layers.normalization import BatchNormalization
from keras.callbacks import ModelCheckpoint
model = Sequential()
model.add(ZeroPadding2D((1,1),input_shape=(3,224,224)))
model.add(Convolution2D(64, 3, 3, activation='relu'))
model.add(ZeroPadding2D((1,1)))
model.add(Convolution2D(64, 3, 3, activation='relu'))
model.add(MaxPooling2D((2,2), strides=(2,2)))
model.add(ZeroPadding2D((1,1)))
model.add(Convolution2D(128, 3, 3, activation='relu'))
model.add(ZeroPadding2D((1,1)))
model.add(Convolution2D(128, 3, 3, activation='relu'))
model.add(MaxPooling2D((2,2), strides=(2,2)))
model.add(ZeroPadding2D((1,1)))
model.add(Convolution2D(256, 3, 3, activation='relu'))
model.add(ZeroPadding2D((1,1)))
model.add(Convolution2D(256, 3, 3, activation='relu'))
model.add(ZeroPadding2D((1,1)))
model.add(Convolution2D(256, 3, 3, activation='relu'))
model.add(MaxPooling2D((2,2), strides=(2,2)))
model.add(ZeroPadding2D((1,1)))
model.add(Convolution2D(512, 3, 3, activation='relu'))
model.add(ZeroPadding2D((1,1)))
model.add(Convolution2D(512, 3, 3, activation='relu'))
model.add(ZeroPadding2D((1,1)))
model.add(Convolution2D(512, 3, 3, activation='relu'))
model.add(MaxPooling2D((2,2), strides=(2,2)))
model.add(ZeroPadding2D((1,1)))
model.add(Convolution2D(512, 3, 3, activation='relu'))
model.add(ZeroPadding2D((1,1)))
model.add(Convolution2D(512, 3, 3, activation='relu'))
model.add(ZeroPadding2D((1,1)))
model.add(Convolution2D(512, 3, 3, activation='relu'))
model.add(MaxPooling2D((2,2), strides=(2,2)))
model.add(Flatten())
model.add(Dense(4096, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(4096, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(28, activation='softmax'))

# if weights_path:
# model.load_weights(weights_path)
# return mode

# model = VGG16(weights='imagenet', include_top=True)
#
# model.layers.pop()
#
# for layer in model.layers[:5]:
#     layer.trainable = False
# modell = Sequential()
# for layer in model.layers:
#     modell.add(layer)
# modell.add(Dense(output_dim=23, activation='softmax'))
model.summary()
from keras.optimizers import SGD

sgd = SGD(lr=1e-3, decay=1e-6, momentum=0.9, nesterov=True)
modell.compile(optimizer=sgd, loss='categorical_crossentropy', metrics=['accuracy'])
from keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(rescale=1. / 255,
                                   shear_range=0.2,
                                   zoom_range=0.2,
                                   horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1. / 255)

training_set = train_datagen.flow_from_directory('PlantVillage-Dataset/raw/color',
                                                 target_size=(224, 224),
                                                 batch_size=32,
                                                 class_mode='categorical')

test_set = test_datagen.flow_from_directory('PlantVillage-Dataset/raw/test',
                                            target_size=(224, 224),
                                            batch_size=32,
                                            class_mode='categorical')
filepath = "gdrive/My Drive/live1.h5"
checkpoint = ModelCheckpoint(filepath, monitor='val_acc', save_best_only=True, mode='max', verbose=1)
from keras.callbacks import EarlyStopping

stop_here_please = EarlyStopping(patience=7)
callbacks_list = [checkpoint, stop_here_please]
modell.fit_generator(training_set,
                     samples_per_epoch=43447 / 32,
                     nb_epoch=50,
                     validation_data=test_set,
                     nb_val_samples=10858 / 32, callbacks=callbacks_list)
modell.save("gdrive/My Drive/hack1.h5")

#testing

from collections import Counter
from keras.models import load_model

model=load_model('gdrive/My Drive/live1.h5')
import numpy as np
from sklearn.metrics import accuracy_score,confusion_matrix
from keras.preprocessing import image
# =============================================================================
# test_image = image.load_img('gdrive/My Drive/test/Pepper,_bell___Bacterial_spot/Bacterial-spot-pepper2.jpg', target_size = (224, 224))
# test_image = image.img_to_array(test_image)
# test_image = np.expand_dims(test_image, axis = 0)
# print(np.argmax(model.predict(test_image)))
# =============================================================================
from keras.preprocessing.image import ImageDataGenerator
test=ImageDataGenerator().flow_from_directory("gdrive/My Drive/Ds",target_size = (224,224),shuffle=False)
# =============================================================================
# a=np.full()
# =============================================================================
a=[]
import numpy as np
result=model.predict_generator(test)
y_pred = np.argmax(result, axis=1)
for i in result:
    a.append(np.argmax(i))

count=0
for i in result:
    if np.argmax(i)==0:
        count+=1
print(count)
print(accuracy_score(test.classes, y_pred))
cm=confusion_matrix(test.classes,y_pred)
print(y_pred)

def plot_confusion_matrix(cm,
                          target_names,
                          title='Confusion matrix',
                          cmap=None,
                          normalize=True):

    import matplotlib.pyplot as plt
    import numpy as np
    import itertools

    accuracy = np.trace(cm) / float(np.sum(cm))
    misclass = 1 - accuracy

    if cmap is None:
        cmap = plt.get_cmap('Blues')

    plt.figure(figsize=(50, 50))
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()

    if target_names is not None:
        tick_marks = np.arange(len(target_names))
        plt.xticks(tick_marks, target_names, rotation=45)
        plt.yticks(tick_marks, target_names)

    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]


    thresh = cm.max() / 1.5 if normalize else cm.max() / 2
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        if normalize:
            plt.text(j, i, "{:0.4f}".format(cm[i, j]),
                     horizontalalignment="center",
                     color="white" if cm[i, j] > thresh else "black")
        else:
            plt.text(j, i, "{:,}".format(cm[i, j]),
                     horizontalalignment="center",
                     color="white" if cm[i, j] > thresh else "black")


    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label\naccuracy={:0.4f}; misclass={:0.4f}'.format(accuracy, misclass))
    plt.show()

plot_confusion_matrix(cm ,
                      normalize    = False,
                      target_names = sorted(files),
                      title        = "Confusion Matrix")