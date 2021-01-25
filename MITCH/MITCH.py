# Imports statements
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import datetime, time
import webbrowser
import re
import wolframalpha
import speech_recognition as sr
import sys
import os


# Defining the PyQt5 Window and setting its size and window Title
app = QApplication(sys.argv)
win = QMainWindow()
win.setFixedSize(710, 410)
win.setWindowTitle("MITCH - My Intelligent Technologically Created Helper")

# ********************** FUNCTION DEFINITIONS (BACK END) ********************** #

# System speaking function
def speak(message):
    return os.system('say' + ' ' + message)

# System greeting function, checks the time and my software will greet me accordingly
def greeting():
    hour = int(datetime.datetime.now().hour)
    if (hour >= 0) and (hour < 12):
        speak("Good Morning!")
    elif (hour >= 12) and (hour < 18):
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("Hello I'm MITCH. Nice to meet you, how can I help you?")

# System date check
def date():
    currentdate = datetime.datetime.now()
    result = currentdate.strftime("%d %b %Y %A")
    l1.setText(result)
    print(result)
    speak(result)

# System time check
def currenttime():
    result = time.strftime("%I:%M:%S %A")
    l1.setText(result)
    print(result)
    speak(result)

# Google search via webbrowser library
def googleSearch(recognize_words):
    cleanword = recognize_words.replace("ask google", "")
    webbrowser.open('https://www.google.com/search?q={}'.format(cleanword))
    result = 'Opening your query in google search engine sir'
    l1.setText(result)
    print(result)
    speak(result)

# Google Maps search via webbrowser library
def location(recognize_words):
    data = recognize_words.split(" ")
    location = ""
    location = location.split(" ")
    for i in range(2, len(data)):
        location.append(data[i])
    place = "  ".join(location)
    result = "Hold on sir, I will show you."
    l1.setText(result)
    print(result)
    speak(result)
    webbrowser.open("https://www.google.nl/maps/place/" + place)

# Website search via webbrowser library
def openWebsite(recognize_words):
    reg_ex = re.search('open (.+)', recognize_words)
    if reg_ex:
        domain = reg_ex.group(1)
        url = "https://www." + domain + ".com"
        webbrowser.open(url)
        speak("done...")
    else:
        speak("website not available")


# This function uses Google Speech Recognition to detect user audio input and turn into text
def say_something():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    try:
        print("You said: " + r.recognize_google(audio))
        my_line.setText(r.recognize_google(audio))
        my_action()
    except:
        print("Google Speech Recognition Could not understand audio")


# This the function that responds to all the commands given by the user
def my_action():

    # This prints the users input into the console
    print(my_line.text())
    statement = my_line.text()
    # checking if the input is valid
    if (len(statement) >= 1):


        if "who are you" in statement:
            l1.setText("I am MITCH a simple virtual assistant.")
            print("I am MITCH a simple virtual assistant.")
            speak("I am MITCH a simple virtual assistant.")

        elif 'hello' in statement:
            l1.setText("hello sir, how are you?")
            print("hello sir, how are you?")
            speak("hello sir, how are you?")

        elif "how are you" in statement:
            l1.setText("I am not the only one here that is having fun with you, it is all me.")
            print("I am not the only one here that is having fun with you, it is all me.")
            speak("I am not the only one here that is having fun with you, it is all me.")

        elif "what's new" in statement:
            l1.setText("Nothing, I just thought it was a bit of an overreaction. It has been a while since I have read it.")
            print("Nothing. I just thought it was a bit of an overreaction. It has been a while since I have read it.")
            speak("Nothing. I just thought it was a bit of an overreaction. It has been a while since I have read it.")

        elif "that's great" in statement:
            l1.setText("Thank you")
            print("Thank you")
            speak("Thank you")

        elif "thank you" in statement:
            l1.setText("You are welcome")
            print("you're welcome")
            speak("you're welcome")

        elif "you are welcome" in statement:
            l1.setText("my pleasure")
            print("my pleasure")
            speak("my pleasure")

        elif "where are you from" in statement:
            l1.setText("Magical place call Toronto")
            print("Magical place call Toronto")
            speak("Magical place call Toronto")

        elif "who made you" in statement:
            l1.setText("Moayyad Shahid, you do not find him he finds you")
            print("Moayyad Shahid, you do not find him he finds you")
            speak("Mo ay yad Sha hid, you do not find him he finds you")

        # using the date function to give the user the date
        elif "what is date" in statement:
            date()

        # using the time function to give the user the current time
        elif "what is time" in statement:
            currenttime()

        # using the googleSearch function for the desired query
        elif "ask google" in statement:
            googleSearch(statement)

        # using location function to pop up the google maps location
        elif "where is" in statement:
            location(statement)

        # using the openWebsite function to open the desired website
        elif "open" in statement:
            openWebsite(statement)

        # using the built-in quit function to give close the program
        elif "goodbye" in statement:
            print("See you later, bye")
            speak("See you later, bye")
            quit()

        # If all cases fail then wolfram API is then used to find query results, such as mathematics, weather, etc.
        else:
            my_app_id = wolframalpha.Client('QHR7WJ-52AL3EQWU4')
            res = my_app_id.query(statement)
            ans = next(res.results).text
            l1.setText(ans)

            y = ans
            os.system('espeak "{}"'.format(y))

    # If everything fails, then program claims that it is limited
    else:
        print("not working")
        l1.setText("not working, my capacities are limited at the moment")
        speak("not working, my capacities are limited at the moment")

#************************* FRONT END WIDGET DEFINITIONS ************************#

# INPUT TEXT BOX
my_line = QtWidgets.QLineEdit(win)
my_line.setPlaceholderText('Ask Me Anything...')
my_line.returnPressed.connect(my_action)
my_line.resize(600, 25)
my_line.move(30, 20)


# BUTTON WIDGET
b1 = QtWidgets.QPushButton(win)
b1.setText("Speak")
b1.clicked.connect(say_something)
b1.setFixedSize(60, 25)
b1.move(640, 20)

# OUTPUT TEXT BOX
l1 = QtWidgets.QTextEdit(win)
l1.move(30, 50)
l1.setFixedSize(600, 300)

# BOTTOM SIGNATURE
l2 = QtWidgets.QLabel(win)
l2.setText("Courtesy of Moayyad Shahid")
l2.move(260, 335)
l2.resize(550, 100)

# START OFF WITH GREETING
greeting()

# LAUNCHES WINDOW
win.show()
sys.exit(app.exec_())
