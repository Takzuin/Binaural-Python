import numpy as np
import sounddevice as sd


def generate_binaural_tone(freq_left, freq_right, duration, sample_rate=154100, volume=0.4):
    """
    Genera un sonido binaural reproducible.

    :param freq_left: Frecuencia para el canal izquierdo (Hz)
    :param freq_right: Frecuencia para el canal derecho (Hz)
    :param duration: Duración del sonido (segundos)
    :param sample_rate: Tasa de muestreo (Hz)
    :param volume: Volumen (0.0 a 1.0)
    """
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)

    # Crear ondas sinusoidales para cada canal
    wave_left = np.sin(2 * np.pi * freq_left * t) * volume
    wave_right = np.sin(2 * np.pi * freq_right * t) * volume

    # Combinar en un arreglo estéreo (dos canales)
    stereo_wave = np.stack([wave_left, wave_right], axis=1)

    return stereo_wave


# Parámetros del sonido binaural
freq_left = 528  # Frecuencia del canal izquierdo (Hz)
freq_right = 538  # Frecuencia del canal derecho (Hz)
duration = 15  # Duración en segundos

# Generar el sonido
binaural_sound = generate_binaural_tone(freq_left, freq_right, duration)

# Reproducir el sonido
sd.play(binaural_sound, samplerate=44100)
sd.wait()
