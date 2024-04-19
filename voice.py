
"""
pkg install play-audio
pip install gtts
"""
import os
try:
    import gtts
except:
    
    os.system("pip install gtts")
    import gtts
from gtts import gTTS

def create_(text,file):
    my_a = gTTS(text)
    my_a.save(file)


def play_audio(audio_file):
    os.system("play-audio "+audio_file)
    

def dual(text,file):
    create_(text,file)
    play_audio(file)

dual("hello sir ,I am your assistant","l.mp3")