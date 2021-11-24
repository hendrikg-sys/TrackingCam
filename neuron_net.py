from keras import *
from tensorflow import *
from keras import *
from numpy import array

model = models.Sequential()

input = [1, 2, 3, 4, 5]

output = [3, 6, 9, 12, 15]


model.add(layers.Dense(units=3, input_shape=[1]))

model.add(layers.Dense(units=2))

model.add(layers.Dense(units=1))


model.compile(loss="mean_squared_error", optimizer="sgd")

model.fit(x=input, y=output, epochs=10000)

print(model.predict([68]))
