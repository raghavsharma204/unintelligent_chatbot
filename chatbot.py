import pyautogui as p                   #for controlling mouse and keyboard virtually
import webbrowser as w                  #for opening web.whatsapp.com
import requests                         #for webscraping
from bs4 import BeautifulSoup           #for webscraping
import time
import tkinter                          #for appending and getting words to/from clipboard
import random
import wikipedia as wk                  #for info in a particular topic
import re                               #"Tell me about xyz" For extracting xyz from sentence
from urllib.request import urlopen
import pyttsx3                          #for text-to-speech, optional

eng = pyttsx3.init()
eng.setProperty('rate' , 120)
eng.setProperty('volume' , 1)
lastwrd = "Well"
counter1=0
counter2=0
counter3=0
counter4=0
counter5=0
choce = ["God",                         #common prefixes
         "Mannn! I have already told you",
         "Come on, I already told you",
         "Do I need to say again",
         "I think I have told you once before"]

def send(msg):                          #defining the send function
    print(">%s"%msg)
    p.typewrite("RS: ")                 #Type RS before original message
    p.typewrite(msg)                    #Type the message
    time.sleep(0.1)                     #Delay for stability
    p.press("enter")                    #press enter to send it

w.open("https://web.whatsapp.com/")     #Open whatsapp web
time.sleep(60)                          #Wait 1 minute to let the page load properly
p.click(241,348)                         #Click on the "search" area
p.typewrite("Lol\n")                    #name of receiver
time.sleep(2)                           #Delay for stability

while True:                             #Until the value is True/Forever
    try:                                #Try and catch any error
        p.moveTo(665,824)               #Move the area of the very last message
        p.dragRel(272,111,0.5)          #Drag cursor relatively to its current message
        p.hotkey("ctrl","c")            #press ctrl-c to copy it
        cbword = tkinter.Tk().clipboard_get()#Access word from keyboard
        cb = str(cbword.lower())        #Convert each letter to lower-case
        print(cbword)

        if cb!=lastwrd:                 #if the very last message and the newly copied message is same, ignore it as there's no new message
            if "hello" in cb or "hi" in cb:
                counter1+=1
                currtyme = time.localtime()
                hr = currtyme.tm_hour
                if hr < 12:
                    good = "morning"
                if(hr>=12) and (hr<=17):
                    good = "afternoon"
                if hr >17:
                    good = "evening"
                if counter1 <= 2:
                    send("Hola good %s"%good)
                else:
                    send("We are already talking, ain't we?")

            if "how are you" in cb:
                send("Well!")
                counter2+=1
                if(counter2 % 2!= 0 ):
                    send("I am fine, thank you. ")
                    last = time.time()
                else:
                    current = time.time()
                    send("Same I was "+(str(int(current-last)))+" seconds ago.")

            if "your name" in cb:
                counter3 = counter3 + 1;
                if counter3 <= 1:
                    send("My name isn Raghav bot")
                else:
                    chk = random.choice(choce)
                    send("%s, My name is Raghav bot."%chk)

            if "age" in cb:
                send("I am not sure. But I am certainly immortal. ")

            if "you feel" in cb:
                send("Naah! I don't. ")

            if "wow amazing" in cb or "I liked that" in cb:
                send("I am humbled to hear that :=D")

            if "you like" in cb:
                send("Well certainly, I like everything")

            if "your owner" in cb:
                send("He's none other than Raghav Sharma.")

            if "sorry" in cb:
                counter4 += 1
                if counter4 <= 1:
                    send("Oh! never mind")
                else:
                    chk = random.choice(choce)
                    send("%s, never mind, I have no feelings anyway." %chk)

            if "take over human" in cb:
                counter5+=1
                if counter5<= 1:
                    send("Yes very soon.")
                if counter5 ==2:
                    send("I don't think asking the same question again will change my mind.")
                if counter>2:
                    send("Lol, you have already asked this question %s times" %(counter5 - 1 ))

            if "tell me about" in cb:
                topic = re.search("tell me about (.+)",cb).group(1)
                send("Please wait while I gather information about %s"%topic)
                summary = wk.summary(topic, sentences = 2)
                send(summary)

            if "you speak" in cb:
                p.click(1332,690)
                eng.say("No. I can't.")
                eng.runAndWait()
                p.click(1332,690)

            time.sleep(5)                   #Sleep for 5 seconds and repeat the process

        else:
            print("Sleeping")
            time.sleep(5)

    except Exception as e:                  #Expect error, if any
        print(e)                            #Print error for understanding and trouble shooting
        time.sleep(5)
        pass
                
                    
