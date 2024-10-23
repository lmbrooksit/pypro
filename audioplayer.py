import sounddevice as sd
import numpy as np
from pydub import AudioSegment


def read_audio(file_path):
    audio = AudioSegment.from_file(file_path)
    data = np.array(audio.get_array_of_samples())

    # Convert stereo to mono if necessary
    if audio.channels == 2:
        data = data.reshape((-1, 2))
        data = data.mean(axis=1)  # Average the two channels
    return data, audio.frame_rate


def play_tracks(tracks):
    max_length = max(len(track) for track in tracks)
    mixed = np.zeros(max_length, dtype=np.float32)

    for track in tracks:
        mixed[:len(track)] += track.astype(np.float32) / np.max(np.abs(track))  # Normalize

    sd.play(mixed, samplerate=44100)
    sd.wait()  # Wait until playback is finished


if __name__ == "__main__":
    try:
        track1, rate1 = read_audio('rap.wav')
        track2, rate2 = read_audio('song.wav')

        if rate1 != rate2:
            print("Sample rates do not match!")
        else:
            play_tracks([track1, track2])

    except Exception as e:
        print(f"An error occurred: {e}")
