import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# dataset path
train_dir = "../dataset"

# data
datagen = ImageDataGenerator(rescale=1./255, validation_split=0.2)

train = datagen.flow_from_directory(
    train_dir,
    target_size=(128,128),
    batch_size=8,
    subset="training"
)

val = datagen.flow_from_directory(
    train_dir,
    target_size=(128,128),
    batch_size=8,
    subset="validation"
)

# simple model
model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(32, (3,3), activation='relu', input_shape=(128,128,3)),
    tf.keras.layers.MaxPooling2D(),

    tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(),

    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(train.num_classes, activation='softmax')
])

model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# train
model.fit(train, validation_data=val, epochs=5)

# save (IMPORTANT)
model.save("leaf_model.keras")

print("DONE")