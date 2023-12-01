import sys
import os
from pydub import AudioSegment
from pydub.playback import play
import tensorflow as tf
from tensorflow import keras
import turtle

def main():
    # Read parameters from Command Line
    directory = sys.argv[1]

        trimmer(directory)

 
    perform_machine_learning()

    
    draw_square()

def trimmer(directory):
    for root, dirs, files in os.walk(directory):
        for name in files:
            if name.endswith(".mp3"):
                trim_metadata(root + "/" + name)

        for name in dirs:
            trimmer(name)

def trim_metadata(file_path):
    audio = AudioSegment.from_file(file_path, format="mp3")

    artist = audio.get_metadata("artist")
    title = audio.get_metadata("title")

    if artist:
        artist = artist.strip()
        audio = audio.set_metadata("artist", artist)

    if title:
        title = title.strip()
        audio = audio.set_metadata("title", title)

    audio.export(file_path, format="mp3")

def perform_machine_learning():
  
    x_train = tf.random.normal((100, 10))
    y_train = tf.random.randint(2, size=(100, 1))

    
    model = keras.Sequential([
        keras.layers.Dense(64, activation='relu', input_shape=(10,)),
        keras.layers.Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])


    model.fit(x_train, y_train, epochs=5)

def draw_square():
    turtle.speed(2)
    for _ in range(4):
        turtle.forward(100)
        turtle.right(90)
    turtle.done()

if __name__ == '__main__':
    main()
