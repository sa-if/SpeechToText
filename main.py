import speech_recognition as sr
import pydub
from pydub import AudioSegment
from nltk import pos_tag
import os

# create a recognizer object
r = sr.Recognizer()

# open the audio file
try:
    # convert the audio file to a format that can be recognized by the SpeechRecognition library
    sound = AudioSegment.from_file('input.wav', format="wav")
    sound.export("temp.wav", format="wav")

    with sr.AudioFile("temp.wav") as source:
        # read the audio data from the file
        audio_data = r.record(source)

        # recognize speech using Google Speech Recognition
        text = r.recognize_google(audio_data)

        # print the recognized text
        print(text)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
except FileNotFoundError:
    print("File not found")
except Exception as e:
    print("Error occurred: {0}".format(e))
finally:
    # delete the temporary file
    os.remove("temp.wav")
