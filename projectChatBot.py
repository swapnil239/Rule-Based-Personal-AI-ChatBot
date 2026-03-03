# Rule Based Basic AI Chatbot in Python

import datetime
import time

name = input("Welcome! Please Enter Your Name:")
presentHour = datetime.datetime.now().hour

if 5 <= presentHour <= 12:
   print("Good Morning!" ,name)
elif 12 <= presentHour <= 18:
      print("Good Evening!", name)
else:
      print("Good night!" ,name)


print("Namaste ! Welcome to Your ChatBot Buddy")
print("Hey ! You can ask me basic question, Type Goodbye to exit from Bot")

# ChatBot Memory Creation ( dictionary of responses)

responses = {
    "Hello": "Hi, Welcome How can i help you?",
    "Who are you" : "I'm your personal Chatbot buddy!",
    "How are you" : "I'm good !",
    "I am not well" : "Oh! don't worry you will get well soon!",
    "Please motivate me": "Oh! Always believe in yourself \n never give up \n Trust the process you will do miracle",
    "I want to learn python list" : "Go and watch python tutorials on Youtube \n and gfg ",
    "Captial of India" : "New Delhi",
    "Prime minister and President of India": "Narendra Modi and smt. Droupadi Murmu",
    "Why Agra City is Famous" : "The Beautiful Taj Mahal which is seventh wonder of the world!",
    "Oldest Religion of the World" : "Hinduism( 2000 - 1500 BCE)"
}

# Function to get response of chatbot

def getResponseOfBot(userQuestion):
    userQuestion = userQuestion.lower()
    for eachKey in responses:
        if eachKey.lower() in userQuestion:
            return responses[eachKey]
        
       # return "I am not aware about it yet! beacuse i'm still in learning mode"

# Take user form input

while True:
 userInput = input("Please Ask Your Questions!")
 reply = getResponseOfBot(userInput) 
 print("Bot Response: ", reply)

 if "Goodbye" in userInput.lower():
    break
