import numpy

# keras 2.1.3 backend tensorflow
# Epoch 1/10 - 7s - loss: 1.3220 - acc: 0.6916 - val_loss: 0.7795 - val_acc: 0.8502
#
from keras.datasets import mnist
#from keras.models import Sequential
#from keras.layers import Dense
from keras.utils import np_utils

# tensorflow 1.4.1
# Epoch 1/5 7s - loss: 13.2108 - acc: 0.1737 - val_loss: 12.5411 - val_acc: 0.2148
#
#from tensorflow.python.keras.datasets import mnist
from tensorflow.python.keras.models   import Sequential
from tensorflow.python.keras.layers   import Dense
#from tensorflow.python.keras          import utils as np_utils


# Устанавливаем seed для повторяемости результатов
numpy.random.seed(42)

# Загружаем данные
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# Преобразование размерности изображений
X_train = X_train.reshape(60000, 784)
X_test = X_test.reshape(10000, 784)
# Нормализация данных
X_train = X_train.astype('float32')
X_test = X_test.astype('float32')
X_train /= 255
X_test /= 255

# Преобразуем метки в категории
Y_train = np_utils.to_categorical(y_train, 10)
Y_test = np_utils.to_categorical(y_test, 10)

# Создаем последовательную модель
model = Sequential()

# Добавляем уровни сети
model.add(Dense(800, input_dim=784, activation="relu", kernel_initializer="normal"))
model.add(Dense(10, activation="softmax", kernel_initializer="normal"))

# Компилируем модель
model.compile(loss="categorical_crossentropy", optimizer="SGD", metrics=["accuracy"])

print(model.summary())

# Обучаем сеть
model.fit(X_train, Y_train, batch_size=200, epochs=5, validation_split=0.2, verbose=2)

# Оцениваем качество обучения сети на тестовых данных
scores = model.evaluate(X_test, Y_test, verbose=0)
print("Точность работы на тестовых данных: %.2f%%" % (scores[1]*100))
