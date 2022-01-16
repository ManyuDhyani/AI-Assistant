import speech_recognition as sr
from gtts import gTTS  # google text to speech
import os  # to save/open files
import webbrowser as wb
import wikipedia
import subprocess
from pygame import mixer
import time


def msg():
    msg = "Done"
    language = "en"
    message = gTTS(text=msg, lang=language, slow=False)
    message.save("message.mp3")
    mixer.init()
    mixer.music.load("message.mp3")
    mixer.music.play()


def process_text(input):
    try:
        if 'open' in input:
            open_application(input)

        elif 'wikipedia' in input:
            wiki(input)
    

        elif 'search' in input or 'play' in input:
            # a basic web crawler using selenium
            search_web(input)
        else:
            pass
            
    except:
        pass


def search_web(input):
    str1 = ""
    if 'search' in input:
        input = input.replace("search", "")
        str1.join(input)
        #assistant_speaks("Searching " + input + ".")
        f_text = 'https://www.google.co.in/search?q=' + input
        wb.open_new_tab(f_text)
        msg()

    if 'play' in input:
        input = input.replace("play", "")
        str1.join(input)
        #assistant_speaks("Playing " + input + " on Youtube.")
        f_text = 'http://www.youtube.com/results?search_query=' + input
        wb.open_new_tab(f_text)
        msg()

# function used to open application
# present inside the system.

def open_application(input):
    if "chrome" in input:
        subprocess.call(["open", "-a", "Google Chrome"])
        msg()

    elif "safari" in input:
        subprocess.call(["open", "-a", "Safari"])
        pmsg()

    elif "pages" in input:
        subprocess.call(["open", "-a", "Pages"])
        msg()

    elif "sublime text" in input:
        subprocess.call(["open", "-a", "Sublime Text"])
        msg()

    elif "terminal" in input:
        subprocess.call(["open", "-a", "Terminal"])
        msg()

    elif "finder" in input:
        subprocess.call(["open", "-a", "Finder"])
        msg()

    elif "mail" in input:
        subprocess.call(["open", "-a", "Mail"])
        msg()

    else:
        print("Try Again!")


def wiki(input):
    str1 = ""

    if 'wikipedia' in input:
        input = input.replace("wikipedia", "")
        str1.join(input)

    #assistant_speaks("Searching " + input + " on wikipedia.")
    try:
        l = wikipedia.search(input)
        print(l)
        input = l[0]
        p = wikipedia.summary(input, sentences=2)
        print(p)
        language = "en"
        wiki = gTTS(text=p, lang=language, slow=False)
        wiki.save("wiki.mp3")
        mixer.init()
        mixer.music.load("wiki.mp3")
        mixer.music.play()
        time.sleep(15)
    except:
        pass
    



#process_text("search xyz")



