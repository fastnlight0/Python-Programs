# Importing the dataset with Keras and transforming it
from keras.datasets import mnist
from keras import backend as K
def mnist_data():
    # input image dimensions
    img_rows, img_cols = 28, 28
    (X_train, Y_train), (X_test, Y_test) = mnist.load_data()
    if K.image_data_format() == 'channels_first':
        X_train = X_train.reshape(X_train.shape[0], 1, img_rows, img_cols)
        X_test = X_test.reshape(X_test.shape[0], 1, img_rows, img_cols)
        input_shape = (1, img_rows, img_cols)
    else:
        X_train = X_train.reshape(X_train.shape[0], img_rows, img_cols, 1)
        X_test = X_test.reshape(X_test.shape[0], img_rows, img_cols, 1)
        input_shape = (img_rows, img_cols, 1)
    # rescale [0,255] --> [0,1]
    X_train = X_train.astype('float32')/255
    X_test = X_test.astype('float32')/255
    # transform to one hot encoding
    Y_train = np_utils.to_categorical(Y_train, 10)
    Y_test = np_utils.to_categorical(Y_test, 10)
    return (X_train, Y_train), (X_test, Y_test)
(X_train, Y_train), (X_test, Y_test) = mnist_data()