import numpy as np
import sounddevice as sd
import time

# [in_count,in_hold,out_count,out_hold]
count_object = [{1: 10}, {2: 10}, {3: 10}, {4: 10}]
cycle_object = ["in", "hold", "out", "hold"]

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

num_cycles = 10
base_frequency = 500  # Starting frequency for higher tone
whole_step_factor = 1.12246  # Factor for one whole note step

for h in range(num_cycles):
    print("cycle =", h + 1)

    for i in range(4):
        start_time = time.time()
        play_tone(base_frequency, 0.3)
        elapsed_time = time.time() - start_time
        time.sleep(1 - elapsed_time)  # Ensure 1 second interval

        start_time = time.time()

        number = i + 1
        print("level is:", number, "index is:", i)
        print("count for this level", count_object[i][number])
        current_count = count_object[i][number]

        for j in range(current_count):
            counting = j + 1
            print("counting:", counting)

            start_time = time.time()
            play_tone(base_frequency, 0.2)
            elapsed_time = time.time() - start_time
            time.sleep(1 - elapsed_time)  # Ensure 1 second interval

            next_time = start_time + 1
            while time.time() < next_time:
                pass
            start_time = next_time
        
        base_frequency *= whole_step_factor  # Increase frequency by one whole note for the next cycle
