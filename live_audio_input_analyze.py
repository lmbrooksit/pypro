import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import tkinter as tk
from tkinter import ttk

# Parameters for recording
samplerate = 44100  # Sample rate in Hz
buffer_duration = 2  # Buffer to display 2 seconds of audio
buffer_size = int(samplerate * buffer_duration)
audio_buffer = np.zeros(buffer_size)
recording = False

# Initialize the plot
fig, ax = plt.subplots()
x = np.linspace(0, buffer_duration, buffer_size)
line, = ax.plot(x, audio_buffer)
ax.set_ylim(-1, 1)
ax.set_xlim(0, buffer_duration)
ax.set_title("Live Audio Input")
ax.set_xlabel("Time [s]")
ax.set_ylabel("Amplitude")

# TKinter setup
root = tk.Tk()
root.title("Audio Recorder")
root.geometry("300x100")


def audio_callback(indata, frames, time, status):
    """Callback function to capture audio data."""
    if recording:
        global audio_buffer
        audio_buffer = np.roll(audio_buffer, -frames)
        audio_buffer[-frames:] = indata[:, 0]


def update_plot(frame):
    line.set_ydata(audio_buffer)
    return line,


def start_recording():
    global recording, stream
    if not recording:
        recording = True
        stream.start()


def stop_recording():
    global recording, stream
    if recording:
        recording = False
        stream.stop()


# Start and Stop buttons
start_button = ttk.Button(root, text="Start Recording", command=start_recording)
start_button.pack(side="left", padx=20, pady=20)

stop_button = ttk.Button(root, text="Stop Recording", command=stop_recording)
stop_button.pack(side="right", padx=20, pady=20)

# Stream configuration
stream = sd.InputStream(samplerate=samplerate, channels=1, callback=audio_callback)

# Matplotlib animation
ani = FuncAnimation(fig, update_plot, interval=50, blit=True)


# Main loop for matplotlib and tkinter
def run():
    while True:
        root.update_idletasks()
        root.update()
        plt.pause(0.01)


root.after(0, run)
plt.show()