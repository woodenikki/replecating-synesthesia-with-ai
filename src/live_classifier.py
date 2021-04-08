import os
import json
import math
import librosa
import numpy as np
import tensorflow as tf
import tensorflow.keras as keras
from sklearn.model_selection import train_test_split

# https://www.tensorflow.org/io/tutorials/audio

COLOR_CATEGORIES = ["Black", "Blue", "Brown", "Gray", "Green", "Orange", "Pink", "Purple", "Red", "White", "Yellow"]
TEXTURE_CATEGORIES = ["None", "Smoky", "Smooth", "Soft", "Sparkly", "Spiky", "Woody"]
LUMINOSITY_CATEGORIES = ["Yes", "No"]

SAMPLE_RATE             = 22050                     # music processing value
DURATION                = 30                        # measured in seconds 
SAMPLES_PER_TRACK       = SAMPLE_RATE * DURATION

DATASET_PATH            = "E:\Test"
TEST_SAMPLE             = "E:\Test\classical.00013.wav"
COLOR_MODEL             = "src\models\color300.h5"
TEXTURE_MODEL           = "src\models\texture300.h5"
LUMINOSITY_MODEL        = "src\models\luminisity75.h5"

def load_data(dataset_path, num_segments=10, n_mfcc=13, n_fft=2048, hop_length=512):
    """Extracts MFCCs from music dataset and saves them into a json file along with genre labels.
        :param dataset_path (str): Path to dataset
        :param json_path (str): Path to json file used to save MFCCs
        :param num_mfcc (int): Number of coefficients to extract
        :param n_fft (int): Interval we consider to apply FFT. Measured in # of samples
        :param hop_length (int): Sliding window for FFT. Measured in # of samples
        :param: num_segments (int): Number of segments we want to divide sample tracks into
        :return:
        """
    # build a dictionary to store data
    data = {
        "mapping": [],                                  # "classical" (-> 0), "blues (-> 1), etc...
        "mfcc": [],                                     # training inputs
        "labels": []                                    # training targets [0, 0, 1]
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
                    print("{}, segment:{}".format(file_path, s+1))

    # convert lists to numpy arrays
    inputs = np.array(data["mfcc"])

    return  inputs

if __name__ == "__main__":

    inputs = load_data(DATASET_PATH)
    print(inputs[0].size)
    model = tf.keras.models.load_model(LUMINOSITY_MODEL)
    model.summary()

    print(LUMINOSITY_CATEGORIES[np.argmax(model.predict(inputs), axis=-1)[0]])
    # print(LUMINOSITY_CATEGORIES[np.argmax(model.predict(inputs), axis=-1)[0]])
