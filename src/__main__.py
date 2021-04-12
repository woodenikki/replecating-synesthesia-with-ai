import os
import json
import math
import click
import librosa
import numpy as np
import tensorflow as tf
import tensorflow.keras as keras
from sklearn.model_selection import train_test_split


COLOR_CATEGORIES = ["Black", "Blue", "Brown", "Gray", "Green", "Orange", "Pink", "Purple", "Red", "White", "Yellow"]
TEXTURE_CATEGORIES = ["None", "Smoky", "Smooth", "Soft", "Sparkly", "Spiky", "Woody"]
LUMINOSITY_CATEGORIES = ["Yes", "No"]

DATASET_PATH            = "E:\Test"
COLOR_MODEL             = "src\models\color300.h5"
TEXTURE_MODEL           = "src\\models\\texture300.h5"
LUMINOSITY_MODEL        = "src\models\luminisity75.h5"

@click.command()
@click.option("-s", "--sample", required=False, help="Name of test sample (including .wav) from test_samples folder")
@click.option(
    "-p",
    "--path",
    default="src\\test_samples\\TESTING",
    type=click.Path(file_okay=False, writable=False, exists=True),
    help="Path to find test samples",
)
def main(sample, path):
    
    inputs, names = load_data(path)
    # print(inputs[0].size)

    col_model = tf.keras.models.load_model(COLOR_MODEL)
    col_model.summary()

    tex_model = tf.keras.models.load_model(TEXTURE_MODEL)
    tex_model.summary()

    lum_model = tf.keras.models.load_model(LUMINOSITY_MODEL)
    lum_model.summary()

    song = names[0]
    col = COLOR_CATEGORIES[np.argmax(col_model.predict(inputs), axis=-1)[0]]
    tex = TEXTURE_CATEGORIES[np.argmax(tex_model.predict(inputs), axis=-1)[0]]
    lum_bool = LUMINOSITY_CATEGORIES[np.argmax(lum_model.predict(inputs), axis=-1)[0]]
    if (lum_bool == "Yes"):
        lum = ""
    else:
        lum = " no"

    if (tex == "None"):
        tex = "Untextured"

    print("{} is predicted to be {} {} with{} luminosity".format(song, tex, col, lum))



def load_data(dataset_path, num_segments=10, n_mfcc=13, n_fft=2048, hop_length=512):

    SAMPLE_RATE             = 22050                     # music processing value
    DURATION                = 30                        # measured in seconds 
    SAMPLES_PER_TRACK       = SAMPLE_RATE * DURATION
    # build a dictionary to store data
    data = {
        "mapping": [],                                  # "classical" (-> 0), "blues (-> 1), etc...
        "mfcc": [],                                     # training inputs
        "labels": [],                                   # training targets [0, 0, 1]
        "names": []
    }

    num_samples_per_segment                 = int(SAMPLES_PER_TRACK / num_segments)
    expected_num_mfcc_vectors_per_segment   = math.ceil(num_samples_per_segment / hop_length) # 1.2 -> 2

    # loop through all colors recursively
    for i, (dirpath, dirnames, filenames) in enumerate(os.walk(dataset_path)):      # dirpath = current folder, dirnames = names of subfolders, filenames = all files in dirpath
                                                                                    # enumerate packs the 3 vars and gives it a value for i  
        # process files for a specific genre
        for f in filenames:

            # load audio files
            file_path = os.path.join(dirpath, f) 
            signal, sr = librosa.load(file_path, sr=SAMPLE_RATE)

            # process segments, extract mfcc, store data
            for s in range(num_segments):
                start_sample = num_samples_per_segment * s
                finish_sample = start_sample + num_samples_per_segment 
                
                # extract mfcc
                mfcc = librosa.feature.mfcc(signal[start_sample:finish_sample], sr=sr, n_fft=n_fft, n_mfcc=n_mfcc, hop_length=hop_length)
                mfcc = mfcc.T
                
                # store mfcc & label for segment if it has the expected length
                if len(mfcc) == expected_num_mfcc_vectors_per_segment:
                    data["mfcc"].append(mfcc.tolist())
                    data["labels"].append(i-1)
                    data["names"].append(f) #.split("."[0])
                    print("{}, segment:{}".format(file_path, s+1))

    # convert lists to numpy arrays
    inputs = np.array(data["mfcc"])
    names = np.array(data["names"])

    return  inputs, names



if __name__ == "__main__":
    main()
   