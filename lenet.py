# -*- coding: utf-8 -*-
"""Lenet.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lBa8BEpmX7r2uPbv8mPoJ77TDDd_Z3PW
"""

import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt

ds = keras.datasets.mnist

(train_images, train_labels), (valid_images, valid_labels) = ds.load_data()
test_images, test_labels = valid_images[(len(valid_images)//2):], valid_labels[(len(valid_images)//2):]
valid_images, valid_labels = valid_images[:(len(valid_images)//2)], valid_labels[:(len(valid_images)//2)]

model = keras.Sequential([
    keras.layers.Conv2D(filters = 6, kernel_size = 5, strides = 1, activation="relu", input_shape = (28, 28, 1)),
    keras.layers.AveragePooling2D(pool_size = 2, strides = 2),
    keras.layers.Conv2D(filters = 16, kernel_size = 5, strides = 1, activation="relu"),
    keras.layers.AveragePooling2D(pool_size = 2, strides = 2),
    keras.layers.Flatten(),
    keras.layers.Dense(120, activation = "relu"),
    keras.layers.Dropout(0.1),
    keras.layers.Dense(84, activation = "relu"),
    keras.layers.Dropout(0.1),
    keras.layers.Dense(10)
])

model.compile(optimizer = keras.optimizers.Adam(learning_rate=1e-4) , loss = keras.losses.SparseCategoricalCrossentropy(from_logits=True), metrics=["accuracy"])

model.fit(
    train_images,
    train_labels,
    epochs = 5,
    batch_size = 32,
    verbose = 1,
    validation_data=(valid_images, valid_labels)
)

predictions = model.predict(test_images[:])
metric = keras.metrics.Accuracy()
metric.update_state(test_labels, predictions.argmax(axis = 1))
metric.result().numpy() * 100