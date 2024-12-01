import numpy as np
import sounddevice as sd
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def generate_binaural_tone(freq_left, freq_right, duration, sample_rate, volume):
    """
    Generates a binaural sound wave.

    :param freq_left: Frequency for the left channel (Hz)
    :param freq_right: Frequency for the right channel (Hz)
    :param duration: Duration of the sound (seconds)
    :param sample_rate: Sampling rate (Hz)
    :param volume: Volume (0.0 to 1.0)
    :return: Stereo waveform
    """
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)

    # Create sine waves for each channel
    wave_left = np.sin(2 * np.pi * freq_left * t) * volume
    wave_right = np.sin(2 * np.pi * freq_right * t) * volume

    # Combine into stereo waveform
    stereo_wave = np.stack([wave_left, wave_right], axis=1)

    return stereo_wave

def play_sound():
    try:
        # Get user inputs
        freq_left = float(freq_left_var.get())
        freq_right = float(freq_right_var.get())
        duration = float(duration_var.get())
        sample_rate = int(sample_rate_var.get())
        volume = float(volume_var.get())

        # Validate input values
        if not (0.0 <= volume <= 1.0):
            raise ValueError("Volume must be between 0.0 and 1.0.")
        if duration <= 0:
            raise ValueError("Duration must be greater than 0.")

        # Generate and play sound
        binaural_sound = generate_binaural_tone(freq_left, freq_right, duration, sample_rate, volume)
        sd.play(binaural_sound, samplerate=sample_rate)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def stop_sound():
    try:
        sd.stop()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while stopping the sound: {e}")

# Tkinter GUI
root = tk.Tk()
root.title("Binaural Sound Generator")

# Input fields with labels
fields = [
    ("Left Frequency (Hz):", "400 (Recommended)"),
    ("Right Frequency (Hz):", "410 (Recommended)"),
    ("Duration (s):", "5 (Recommended)"),
    ("Sample Rate (Hz):", "44100 (Standard)"),
    ("Volume (0.0 - 1.0):", "0.5 (Recommended)"),
]

# Variables for user input
freq_left_var = tk.StringVar(value="400")
freq_right_var = tk.StringVar(value="410")
duration_var = tk.StringVar(value="5")
sample_rate_var = tk.StringVar(value="44100")
volume_var = tk.StringVar(value="0.5")

variables = [freq_left_var, freq_right_var, duration_var, sample_rate_var, volume_var]

for i, (label_text, recommendation) in enumerate(fields):
    label = tk.Label(root, text=label_text)
    label.grid(row=i, column=0, padx=5, pady=5, sticky="e")

    entry = ttk.Entry(root, textvariable=variables[i])
    entry.grid(row=i, column=1, padx=5, pady=5)

    recommendation_label = tk.Label(root, text=recommendation, fg="gray")
    recommendation_label.grid(row=i, column=2, padx=5, pady=5, sticky="w")

# Play button
play_button = ttk.Button(root, text="Play Sound", command=play_sound)
play_button.grid(row=len(fields), column=0, columnspan=1, pady=10, padx=5)

# Stop button
stop_button = ttk.Button(root, text="Stop Sound", command=stop_sound)
stop_button.grid(row=len(fields), column=1, columnspan=1, pady=10, padx=5)

root.mainloop()
