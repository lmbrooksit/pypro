import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parameters for recording
samplerate = 44100  # Sample rate in Hz
duration = 10  # Duration in seconds
buffer = 2 * samplerate  # Buffer size (2 seconds)

# Initialize the plot
fig, ax = plt.subplots()
x = np.linspace(0, duration, samplerate * duration)
line, = ax.plot(x, np.zeros_like(x))
ax.set_ylim(-1, 1)
ax.set_xlim(0, duration)
ax.set_title("Audio Input")
ax.set_xlabel("Time [s]")
ax.set_ylabel("Amplitude")


def audio_callback(indata, frames, time, status):
    """ This is called every `blocksize` samples """
    if status:
        print(status)

    # Update the plot with new audio data
    line.set_ydata(indata[:, 0])


# Stream audio from the default input device
stream = sd.InputStream(samplerate=samplerate, channels=1, callback=audio_callback)
stream.start()


def update(frame):
    return line,


ani = FuncAnimation(fig, update, interval=1000 / samplerate, blit=True)
plt.show()

stream.stop()
stream.close()