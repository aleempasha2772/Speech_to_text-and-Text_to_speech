# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 11:10:25 2020

@author: Aleem

"""

# -*- coding: utf-8 -*-


#importing the  library

import speech_recognition as sr
#from gtts import gTTS
#import os
import pyttsx3 
# pyttx3 converts text to speech (offline)


# Initialize recognizer class (for recognizing the speech)
# recognizer belongs Speech_recognition
r = sr.Recognizer()

# Function to convert text to speech
def SpeakText(command): 
	# command is an arguement bitch
	# Initialize the engine 
	engine = pyttsx3.init() 
	engine.say(command) 
	engine.runAndWait() 
# Reading Microphone as source
# listening the speech and store in audio_text variable

with sr.Microphone() as source:
    print("Talk")
    audio_text = r.listen(source)
    print("Time over, thanks")
# recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
    
    try:
        # using google speech recognition
        a = r.recognize_google(audio_text)
        #print("Text: "+r.recognize_google(audio_text))
        #print(a)
        #return a
        print(a)
        aa = str(a)
        
        mytext = aa 
        #myobj = gTTS(text=mytext, lang=language, slow=False)
        #SpeakText(mytext)
        out = "doing boss"
        out1 = "on process boss"
        if(mytext == "get up"):
            SpeakText(out)
            print("the voice :",out)
        elif(mytext == "do it"):
            SpeakText(out1)
            print("the voice is:",out1)
            
    except:
         b = print("Sorry, I did not get that")
         print(b)
         










