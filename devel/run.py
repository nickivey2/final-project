#!/usr/bin/env python
from jarvis import Jarvis

import logging                      #logging module for easy debugging
import speech_recognition as sr     # speech rec module uses google voice recognition api

logger = logging.getLogger(__name__)   #initalizes logger 


def run_loop():   #function looped that recognizes speech
    r = sr.Recognizer()   # r is the recognizer object
    with sr.Microphone() as source:   # while there is a microphone source listen for input
        while True:
            logger.debug("Waiting for user input.")
            audio = r.listen(source) #gets speech and stores it in audio object

            logger.debug("Performing Speach to text.")

            try:
                result = r.recognize_google(audio,key=None)  # speech recognition result
                Jarvis.handle(result) #sends result to Jarvis.py for handling
            except sr.UnknownValueError:  # Error handling
                logger.debug("Could not understand audio")
            except sr.RequestError as e:  # Error with api
                logger.warn("Could not fetch results from speech to text: " + str(e))
            except Exception as e: # Error Handling
                logger.error("Error processing: " + str(e))

def main(): # Main function 
    logging.basicConfig(format='%(asctime)s %(filename)s:%(lineno)s [%(levelname)s] %(message)s', level=logging.DEBUG)
    run_loop()

if __name__ == '__main__': # initializes and sets main function as main 
    main()