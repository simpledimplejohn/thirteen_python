import numpy as np
import sounddevice as sd
import threading
import time

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

def tone_scheduler(frequency, duration, interval=1):
    """
    Schedule the tone to play at regular intervals.
    
    Args:
        frequency (float): Frequency of the tone in Hertz.
        duration (float): Duration of the tone in seconds.
        interval (float): Interval at which to play the tone in seconds.
    """
    next_time = time.time()
    while True:
        next_time += interval
        play_tone(frequency, duration)
        time.sleep(max(0, next_time - time.time()))

if __name__ == "__main__":
    frequency = 400  # Frequency of the tone in Hertz
    duration = 0.2   # Duration of the tone in seconds

    # Start the tone scheduler in a separate thread
    tone_thread = threading.Thread(target=tone_scheduler, args=(frequency, duration))
    tone_thread.daemon = True  # Allow the thread to exit when the main program exits
    tone_thread.start()

    # Keep the main program running
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Exiting...")
