
#!/usr/bin/env python
import logging
import os
import sys
import datetime
import pyttsx
import pyowm
import webbrowser

logger = logging.getLogger(__name__) #initalizes logger

class Jarvis(object): 
    stopListeningStrings = ["go away", "stop listening", "shut down"] # strings that trigger shutdown

    @classmethod
    def handle(cls, command, **kwargs): #handler function takes speech rec result
        command = command.lower()       #  speech recognized set to lowercase command variable

        logger.debug("Speech Recognized: '%s'", command) #print speech via logger

        if any(stopCom in command for stopCom in cls.stopListeningStrings): # if command contains any string from stopListening
            textToSpeech.speech("Enjoy your day, sir.") # using osx terminal speech to text say text
        elif ("what's your name" in command):
            textToSpeech.speech("my name is jarvis")
        elif ("the time" in command):
            textToSpeech.speech("it is "+ datetime.datetime.now().strftime("%I:%M%p"))
        elif ("the date" in command or "today's date" in command):
            textToSpeech.speech("today is "+ datetime.date.today().strftime("%B %d, %Y"))
        elif ("weather" in command or "going to rain" in command):
           """Weather API"""
           owm = pyowm.OWM('a7303bd853b6a284fb6f1220505dd2bb') #using PYOWM fetch orlando weather 
           observation = owm.weather_at_place('Orlando,FL')
           w = observation.get_weather() # sets w to json result of weather
           print(w)                  
           textToSpeech.speech("it is currently "+str(int(w.get_temperature('fahrenheit')['temp']))+" degrees with "+w.get_detailed_status()+" . The high today is "+str(int(w.get_temperature('fahrenheit')['temp_max']))+" degrees and the low is "+str(int(w.get_temperature('fahrenheit')['temp_min']))+" degrees, with humidity at "+str(int(w.get_humidity()))+" percent")
        elif ("google" in command or "look up" in command):
            """Google Lookup"""
            command = command.replace(' ','+')  #replaces spaces in string with + for google search
            command = command.replace('google','') # removes google from string
            webbrowser.open('https://www.google.com/search?q='+command) #uses webbrowser module to open google search query
        else:
            textToSpeech.speech("Yes sir?")

    
class textToSpeech(object):
    @staticmethod
    def speech(command): #static function to turn text to speach
        if sys.platform.startswith('win'): # if windows computer use pyttsx module for speech
            speech_engine = pyttsx.init('sapi5') 
            speech_engine.setProperty('rate', 150)
            speech_engine.say(command)
            speech_engine.runAndWait()
        else:                           # if not use say command in terminal to speak
            os.system("say "+command);


