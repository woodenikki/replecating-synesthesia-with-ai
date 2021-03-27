import numpy as np
import librosa, librosa.display
import matplotlib.pyplot as plt

# converting an audio file a spectogram / MFCC using fft, stft

FIG_SIZE = (15,10)

file = "practice\4.prep.py"

# load file
signal, sample_rate = librosa.load(file, sr=22050)      # sampleRate * T -> 22050 * 30s

# display waveform
# librosa.display.waveplot(signal, sample_rate, alpha=0.4)
# plt.xlabel("Time (s)")
# plt.ylabel("Amplitude")
# plt.title("Waveform")
# plt.show()

# fft -> specrum
fft = np.fft.fft(signal)
magnitude = np.abs(fft)                                 # indicate the contribution of each frequency to the overall sound
frequency = np.linspace(0, sample_rate, len(magnitude)) # gives n (len(mag) ) equally spaced values from 0 to sr

left_frequency = frequency[:int(len(frequency)/2)]      # only consider first half so we don't repeat
left_magnitude = magnitude[:int(len(magnitude)/2)]

# display spectrum
# plt.plot(left_frequency, left_magnitude)
# plt.xlabel("Frequency")
# plt.ylabel("Magnitude")
# plt.show()

# stft (short time fourier transform) -> spectogram
n_fft = 2048            # number of samples per fft
hop_length = 512        # amount we are shifting to the fft to the right

stft = librosa.core.stft(signal, hop_length=hop_length, n_fft=n_fft)

spectogram = np.abs(stft)
log_spectogram = librosa.amplitude_to_db(spectogram)    #apply a logarithm to transform amplitude to decibels - makes it more intelligable

# librosa.display.specshow(spectogram, sample_rate, hop_length)
# plt.xlabel("Time")
# plt.ylabel("Frequency")
# plt.colorbar()
# plt.show()

# MFCC
MFCCs = librosa.feature.mfcc(signal, n_fft=n_fft, hop_length=hop_length, n_mfcc=13) # 13 is commonly used for music
librosa.display.specshow(MFCCs, sample_rate, hop_length)
plt.xlabel("Time")
plt.ylabel("Frequency")
plt.colorbar()
plt.show()