import os
import azure.cognitiveservices.speech as speechsdk
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wavfile

# Set your Azure subscription and service key
subscription_key = '1572761a3ec942c293f1f817b24c049e'
service_region = 'eastus'  # e.g., 'eastus'

# Configure the speech SDK
speech_config = speechsdk.SpeechConfig(subscription=subscription_key, region=service_region)

# Create a speech recognizer
speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)

# Define a callback function to handle recognized text
def on_recognized(evt):
    print("Recognized: {}".format(evt.result.text))

# Wire up the recognized event to the callback
speech_recognizer.recognized.connect(on_recognized)

# Start audio recording
print("Recording audio. Press Enter to stop...")
input()

# Stop audio recording
speech_recognizer.stop_continuous_recognition()

# Record audio using sounddevice
duration = 25  # Duration of recording in seconds
fs = 44100  # Sample rate (samples per second)
audio_data = sd.rec(int(duration * fs), samplerate=fs, channels=1)
sd.wait()

# Save the recorded audio as a .wav file
output_file = 'shoaib_uddin.wav'
wavfile.write(output_file, fs, audio_data)

print(f"Audio saved as {output_file}")

# Close the recognizer
speech_recognizer.close()
