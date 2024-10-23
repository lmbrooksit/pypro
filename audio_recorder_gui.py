import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.io.wavfile import write
import tkinter as tk
from tkinter import ttk, filedialog


# Parameters for recording
samplerate = 44100  # Sample rate in Hz
buffer_duration = 2  # Buffer to display 2 seconds of audio
buffer_size = int(samplerate * buffer_duration)
audio_buffer = np.zeros(buffer_size)
audio_data = []  # List to store recorded audio data
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
root.geometry("300x150")


def audio_callback(indata, frames, time, status):
    """Callback function to capture audio data."""
    if recording:
        global audio_buffer
        audio_buffer = np.roll(audio_buffer, -frames)
        audio_buffer[-frames:] = indata[:, 0]
        audio_data.append(indata.copy())


def update_plot(frame):
    line.set_ydata(audio_buffer)
    return line,


def start_recording():
    global recording, stream, audio_data
    if not recording:
        recording = True
        audio_data = []
        stream.start()


def stop_recording():
    global recording, stream
    if recording:
        recording = False
        stream.stop()


def save_recording():
    if audio_data:
        audio_array = np.concatenate(audio_data, axis=0)
        file_path = filedialog.asksaveasfilename(defaultextension=".wav",
                                                 filetypes=[("WAV files", "*.wav")])
        if file_path:
            write(file_path, samplerate, audio_array)
            print(f"Recording saved to {file_path}")


# Start and Stop buttons
start_button = ttk.Button(root, text="Start Recording", command=start_recording)
start_button.pack(side="left", padx=10, pady=20)

stop_button = ttk.Button(root, text="Stop Recording", command=stop_recording)
stop_button.pack(side="right", padx=10, pady=20)

save_button = ttk.Button(root, text="Save Recording", command=save_recording)
save_button.pack(side="bottom", padx=10, pady=20)

# Stream configuration
stream = sd.InputStream(samplerate=samplerate, channels=1, callback=audio_callback)

# Matplotlib animation
ani = FuncAnimation(fig, update_plot, interval=50, blit=True, cache_frame_data=False)


# Main loop for matplotlib and tkinter
def run():
    while True:
        root.update_idletasks()
        root.update()
        plt.pause(0.01)


root.after(0, run)
plt.show()