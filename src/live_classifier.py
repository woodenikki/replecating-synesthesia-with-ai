import librosa
import tensorflow as tf

# https://www.tensorflow.org/io/tutorials/audio

COLOR_CATEGORIES = ["Black", "Blue", "Brown", "Gray", "Green", "Orange", "Pink", "Purple", "Red", "White", "Yellow"]
TEXTURE_CATEGORIES = ["None", "Smoky", "Smooth", "Soft", "Sparkly", "Spiky", "Woody"]
LUMINOSITY_CATEGORIES = ["Yes", "No"]

SAMPLE_RATE             = 22050                     # music processing value
DURATION                = 30                        # measured in seconds 
SAMPLES_PER_TRACK       = SAMPLE_RATE * DURATION

TEST_SAMPLE             = "src\test_samples\classical.00013.wav"
COLOR_MODEL             = "src\models\color300.h5"
TEXTURE_MODEL           = "src\models\texture300.h5"
LUMINOSITY_MODEL        = "src\models\luminisity75.h5"

def prepare(file_path):

    # build a dictionary to store data
    data = {
        "mapping": [],                                  # "classical" (-> 0), "blues (-> 1), etc...
        "mfcc": [],                                     # training inputs
        "labels": []                                    # training targets [0, 0, 1]
    }

    num_segments = 5
    num_samples_per_segment = int(SAMPLES_PER_TRACK / num_segments)
    n_mfcc = 13 
    n_fft = 2048
    hop_length = 512


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

if __name__ == "__main__":
    model = tf.keras.models.load_model(COLOR_MODEL)

    prediction = model.predict([prepare(TEST_SAMPLE)])
    print( COLOR_CATEGORIES[int(prediction[0][0])])