import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parameters for recording
samplerate = 44100  # Sample rate in Hz
duration = 10  # Duration in seconds
buffer_size = int(samplerate * duration)  # Buffer size to hold data for visualization

# Initial values for the plot
x = np.linspace(0, duration, buffer_size)
y = np.zeros(buffer_size)

# Initialize the plot
fig, ax = plt.subplots()
line, = ax.plot(x, y)
ax.set_ylim(-1, 1)
ax.set_xlim(0, duration)
ax.set_title("Live Audio Input")
ax.set_xlabel("Time [s]")
ax.set_ylabel("Amplitude")

# Buffer to store the audio data
audio_buffer = np.zeros(buffer_size)


def audio_callback(indata, frames, time, status):
    """ This is called every `blocksize` samples """
    if status:
        print(status)

    global audio_buffer
    # Roll the buffer to the left and add new data at the end
    audio_buffer = np.roll(audio_buffer, -frames)
    audio_buffer[-frames:] = indata[:, 0]


def update_plot(frame):
    line.set_ydata(audio_buffer)
    return line,


# Stream audio from the default input device
stream = sd.InputStream(samplerate=samplerate, channels=1, callback=audio_callback)

with stream:
    ani = FuncAnimation(fig, update_plot, interval=50, blit=True)
    plt.show()