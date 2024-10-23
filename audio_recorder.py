import sounddevice as sd
import scipy.io.wavfile as wav
import numpy as np


def record_audio(duration, filename, samplerate=44100):
    """
    Records audio and saves it as a WAV file.
    
    Parameters:
    - duration: Duration of the recording in seconds.
    - filename: Name of the output WAV file.
    - samplerate: Sampling rate of the recording.
    """
    print(f"Recording for {duration} seconds...")
    recording = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=2, dtype=np.int16)
    sd.wait()  # Wait until recording is finished
    wav.write(filename, samplerate, recording)
    print(f"Recording saved to {filename}")


if __name__ == "__main__":
    duration = 1000  # Duration in seconds
    filename = "output.wav"
    record_audio(duration, filename)