import pyttsx3
from datetime import datetime
import time

engine= pyttsx3.init('sapi5')
voices= engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)

engine.say("press t, for time, d, for date, and other keys for exit")
engine.runAndWait()
dateortime=input("Input: ")


if dateortime=='t':
    choice='y'
    print("To continue press y or to exit press any other key....")
    while choice=='y':
        timeprg = time.localtime()
        count = 0
        for x in timeprg:
            count += 1
            if count == 4:
                hour = x
            if count == 5:
                min = x
        engine.say(f"The time is {hour} {min} sir")
        engine.say("Should i repeat?")
        engine.runAndWait()
        choice = input("Continue: ")

elif dateortime=='d':
    choice='y'
    print("To continue press y or to exit press any other key....")
    while choice=='y':
        timeprg = time.localtime()
        count = 0
        for x in timeprg:
            count += 1
            if count == 1:
                year = x
            if count == 2:
                month = x
            if count == 3:
                day = x
        engine.say(f"Its {year}, {month}, {day}")
        engine.say("should i repeat?")
        engine.runAndWait()
        choice = input("Continue: ")

else:
    engine.say("Thank you for using me.. bye bye")
    engine.runAndWait()