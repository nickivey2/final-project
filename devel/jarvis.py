import logging
import os
import datetime
import pyowm

logger = logging.getLogger(__name__) #initalizes logger

class Jarvis(object): 
    stopListeningStrings = ["go away", "stop listening", "shut down"] # strings that trigger shutdown

    @classmethod
    def handle(cls, command, **kwargs): #handler function takes speech rec result
        command = command.lower()       #  speech recognized set to lowercase command variable

        logger.debug("Speech Recognized: '%s'", command) #print speech via logger

        if any(stopCom in command for stopCom in cls.stopListeningStrings): # if command contains any string from stopListening
            os.system("say Enjoy your day, sir.") # using osx terminal speech to text say text
        elif ("what's your name" in command):
            os.system("say my name is jarvis")
        elif ("the time" in command):
            os.system("say it is "+ datetime.datetime.now().strftime("%I:%M%p"))
        elif ("the date" in command or "today's date" in command):
            os.system("say today is "+ datetime.date.today().strftime("%B %d, %Y"))
        elif ("weather" in command or "going to rain" in command):
           """Weather API"""
           owm = pyowm.OWM('a7303bd853b6a284fb6f1220505dd2bb') #using PYOWM fetch orlando weather 
           observation = owm.weather_at_place('Orlando,FL')
           w = observation.get_weather() # sets w to json result of weather
           print(w)                  
           os.system("say it is currently "+str(int(w.get_temperature('fahrenheit')['temp']))+" degrees with "+w.get_detailed_status()+" . The high today is "+str(int(w.get_temperature('fahrenheit')['temp_max']))+" degrees and the low is "+str(int(w.get_temperature('fahrenheit')['temp_min']))+" degrees, with humidity at "+str(int(w.get_humidity()))+" percent")
        elif ("google" in command or "look up" in command):
            """Google Lookup"""
        else:
            os.system("say Yes sir?")