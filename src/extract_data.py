# Extract inputs and targets of music dataset for an MLP
import os
import json
import math
import librosa



DATASET_PATH        = "E:\Test"
JSON_PATH           = "data.json"               # in current working folder
SAMPLE_RATE         = 22050                     # music processing value
DURATION            = 30                        # measured in seconds 
SAMPLES_PER_TRACK   = SAMPLE_RATE * DURATION

def save_mfcc(dataset_path, json_path, n_mfcc=13, n_fft=2048, hop_length=512, num_segments=5):
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
        # ensure that we're not at the root level (dataset_path)
        if dirpath is not dataset_path:
            
            # save the semantic label (into mapping.. things like "classical" etc)
            dirpath_components = dirpath.split("/") # genre/blues => ["color", "red"]
            semantic_label = dirpath_components[-1] # last value.. "red"
            data["mapping"].append(semantic_label)
            print("\nProcessing {}".format(semantic_label))

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

    with open(json_path, "w") as fp:    # write to json file
        json.dump(data, fp, indent=4)

if __name__ == "__main__":
    save_mfcc(DATASET_PATH, JSON_PATH, num_segments=10)