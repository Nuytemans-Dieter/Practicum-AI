# -*- coding: utf-8 -*-
"""ChessEvaluation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IT0fxCEdRq8e-k8YojUp0fj2d57i-K33
"""

print("Loading libraries...")

from __future__ import absolute_import, division, print_function, unicode_literals

# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers, models
from sklearn.model_selection import train_test_split

# Helper libraries
import numpy as np
import ast
import matplotlib.pyplot as plt

print("Loading data...")

# Open the data
boardText = open("boardData.txt", "r")  # Open file contents (boards)
valueText = open("valueData.txt", "r")  # Open file contents (values)

# Create neural network input variables
boards = []
values = []

                                    # Read and interpret the data
                                    # Get data of the board
for line in boardText:
  stripped = line.strip('\n')       # Strip the newline character
  arr =  ast.literal_eval(stripped) # Interpret the string as an array, not as a string
  arr = np.array(arr)               # Convert to numpy for the next step
  arr = arr.astype(np.float)        # Convert all contents to float instead of string
  boards.append(arr)                # Append data to the list

                                    # Get data of the board values
for line in valueText:
  stripped = line.strip('\n')       # Strip the newline character
  if stripped == 'None':            # Filter None values
    values.append(float(0))         # Append 0 instead of 'None'
  else: 
    values.append(float(stripped))  # Convert to int and add the data to the list

print("Normalizing data...")
normValues = []
high = max(values, key=abs)
for val in values:
  percentage = val / high
  normValues.append( percentage )

values = normValues

#print("Boards:", boards)            # Print the loaded boards
#print("Values:", values)            # Print the loaded values

print("Selecting training and testing data...")

#train_boards = np.array(boards[2:])
#test_boards = np.array(boards[0:1])

#train_values =  np.array(values[2:])
#test_values =  np.array(values[0:1])

train_boards, test_boards, train_values, test_values = train_test_split(boards, values, test_size=0.10, shuffle= True)
train_boards = np.array(train_boards)
test_boards = np.array(test_boards)
train_values = np.array(train_values)
test_values = np.array(test_values)

print("Creating neural network...")

model = keras.Sequential([
    #keras.layers.Flatten(input_shape=train_boards.shape),
    keras.layers.Dense(128, activation='linear'),
    keras.layers.Dense(128, activation='linear'),
    keras.layers.Dense(128, activation='linear'),
    keras.layers.Dense(100000, activation='softmax')
])

print("Compiling the model...")

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

print("Training and testing the model...")

model.fit(train_boards, train_values, epochs=10)

test_loss, test_acc = model.evaluate(test_boards,  test_values, verbose=2)
print('\nTest accuracy:', test_acc, 'with loss', test_loss)