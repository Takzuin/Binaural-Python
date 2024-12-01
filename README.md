Binaural Audio Generator with Tkinter

This project generates binaural audio tones using Python. Users can adjust parameters such as frequency, duration, sample rate, and volume via a graphical interface built with Tkinter.

Key Features

Generate binaural beats by specifying left and right ear frequencies.

Control the duration, sample rate, and volume of the audio.

Includes recommended values for common use cases.

Easily play and stop the generated sound.

Frequency Ranges for Brainwave States

To use this tool effectively, you can configure the frequencies to generate specific brainwave states. Below are commonly used ranges:

Delta Waves (0.5 - 4 Hz):

Best for deep sleep and relaxation.

Example: Set Left Frequency to 100 Hz and Right Frequency to 103 Hz.

Theta Waves (4 - 8 Hz):

Ideal for meditation and creativity.

Example: Set Left Frequency to 200 Hz and Right Frequency to 204 Hz.

Alpha Waves (8 - 14 Hz):

Promotes relaxation and focus.

Example: Set Left Frequency to 300 Hz and Right Frequency to 308 Hz.

Beta Waves (14 - 30 Hz):

Supports concentration and alertness.

Example: Set Left Frequency to 400 Hz and Right Frequency to 414 Hz.

Gamma Waves (30 - 100 Hz):

Enhances problem-solving and cognition.

Example: Set Left Frequency to 500 Hz and Right Frequency to 530 Hz.

Recommended Parameter Values

Left Frequency (Hz): Start with 400 Hz for general use.

Right Frequency (Hz): Slightly offset from the left frequency (e.g., 410 Hz).

Duration (seconds): 5-10 seconds for short tests; longer durations for extended sessions.

Sample Rate (Hz): 44100 Hz (CD quality).

Volume: 0.5 (mid-level).

How to Use

Launch the application by running the Python script.

Adjust the parameters in the interface:

Enter frequencies for the left and right channels.

Set the duration, sample rate, and volume.

Refer to the recommended values displayed beside each field.

Click Play Sound to start the audio.

Click Stop Sound to halt playback at any time.

Dependencies

This application requires the following Python libraries:

numpy

sounddevice

tkinter (built into Python standard library)

Install missing dependencies with:

pip install numpy sounddevice

Notes

Ensure your system audio is configured for stereo output to experience binaural beats properly.

Use headphones for the best effect.

Experiment with different frequency ranges to explore their effects on focus, relaxation, and creativity.

License

This project is licensed under the MIT License. Feel free to use and modify it as needed!
