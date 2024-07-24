import numpy as np
import sounddevice as sd
import time

# this works for tones

count_array = [10, 13, 9, 7]

def play_tone(frequency, duration, volume=0.5, sample_rate=44100):
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

if __name__ == "__main__":
    start_time = time.time()

    for i in count_array:
        print("level 1, i =", i)
        play_tone(500, 0.3)
        next_time = start_time + 1
        while time.time() < next_time:
            pass
        start_time = next_time
        for j in range(i):
            print("level 2, j =", j, "i =", i)
            play_tone(380, 0.3)
            next_time = start_time + 1
            while time.time() < next_time:
                pass
            start_time = next_time

    print("end tone")
    play_tone(700, 1)
