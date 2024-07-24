import numpy as np
import sounddevice as sd
import time

def play_tone(frequency, duration, volume=0.3, sample_rate=44100):
    """
    Play a tone with a given frequency and duration.
    
    Args:
        frequency (float): Frequency of the tone in Hertz.
        duration (float): Duration of the tone in seconds.
        volume (float): Volume of the tone (0.0 to 1.0).
        sample_rate (int): Sample rate in samples per second.
    """
    # Generate time samples
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    # Generate waveform
    waveform = volume * np.sin(2 * np.pi * frequency * t)
    # Play waveform
    sd.play(waveform, samplerate=sample_rate)
    # Wait until the sound has finished playing
    sd.wait()

num_cycles = 60
initial_frequency = 2000  # Initial frequency for higher tone
half_step_factor = 1.05946  # Factor for one half note step
steps = 13
wait_time = 0.5  # Variable wait time in seconds



for i in range(num_cycles):
    start_time = time.time()
    print("cycle:",i)
    base_frequency = initial_frequency  # Reset frequency at the start of each cycle
    for j in range(steps):
        counting = j + 1
        print("counting:", counting)

        # Play first tone
        start_time = time.time()
        play_tone(base_frequency, 0.1, volume=0.3)
        elapsed_time = time.time() - start_time
        time.sleep(wait_time - elapsed_time)  # Ensure wait_time interval

        # Play second tone at half volume
        start_time = time.time()
        play_tone(base_frequency, 0.1, volume=0.15)
        elapsed_time = time.time() - start_time
        time.sleep(wait_time - elapsed_time)  # Ensure wait_time interval

        base_frequency /= half_step_factor  # Decrease frequency by one half note for the next tone
