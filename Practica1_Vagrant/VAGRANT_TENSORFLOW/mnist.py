import tensorflow as tf
from tensorflow import keras

# Cargar el conjunto de datos MNIST
mnist = keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Normalizar los datos de imagen a valores entre 0 y 1
x_train, x_test = x_train / 255.0, x_test / 255.0

# Crear un modelo de red neuronal secuencial
model = keras.models.Sequential([
  keras.layers.Flatten(input_shape=(28, 28)),
  keras.layers.Dense(128, activation='relu'),
  keras.layers.Dropout(0.2),
  keras.layers.Dense(10)
])

# Compilar el modelo con una función de pérdida y un optimizador
loss_fn = keras.losses.SparseCategoricalCrossentropy(from_logits=True)
model.compile(optimizer='adam', loss=loss_fn, metrics=['accuracy'])

# Entrenar el modelo con los datos de entrenamiento
model.fit(x_train, y_train, epochs=5)

# Evaluar el modelo con los datos de prueba
model.evaluate(x_test,  y_test, verbose=2)