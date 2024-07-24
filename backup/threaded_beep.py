import threading
import time
import pyaudio
import numpy as np
import pyttsx3

def play_tone(frequency, duration, volume=0.5, sample_rate=44100):
    p = pyaudio.PyAudio()

    # Generate samples
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    wave = volume * np.sin(2 * np.pi * frequency * t)

    # Ensure samples are in 16-bit format
    samples = (wave * 32767).astype(np.int16).tobytes()

    # Open audio stream
    stream = p.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=sample_rate,
                    output=True)

    # Play the tone
    stream.write(samples)
    stream.stop_stream()
    stream.close()
    p.terminate()

def beep_every_second():
    while True:
        threading.Thread(target=play_tone, args=(1000, 0.5)).start()
        time.sleep(1)

def say_hello_world():
    engine = pyttsx3.init()
    while True:
        engine.say("hello world")
        engine.runAndWait()
        time.sleep(1)

# Create and start threads
beep_thread = threading.Thread(target=beep_every_second)
tts_thread = threading.Thread(target=say_hello_world)

beep_thread.start()
tts_thread.start()

beep_thread.join()
tts_thread.join()
