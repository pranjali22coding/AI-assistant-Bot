# main_gui.py
from tkinter import *
from PIL import Image, ImageTk
import speech_to_text
import action

root = Tk()
root.title("Doraemon Assistant")
root.geometry("550x675")
root.resizable(False, False)
root.config(bg="#FAF16E")

def ask():
    try:
        ask_val = speech_to_text.speech_to_text()
        bot_val = action.Action(ask_val)
        text.insert(END, "Me --> " + ask_val + "\n")
        if bot_val is not None:
            text.insert(END, "Bot <-- " + str(bot_val) + "\n")
        if bot_val == "ok sir":
            root.destroy()
    except Exception as e:
        text.insert(END, f"Error: {str(e)}\n")

def send():
    send = entry.get()
    bot = action.Action(send)
    text.insert(END, "Me --> " + send + "\n")
    if bot is not None:
        text.insert(END, "Bot <-- " + str(bot) + "\n")
    if bot == "ok sir":
        root.destroy()

def del_text():
    text.delete("1.0", "end")

frame = Frame(root, bg="#FAF16E", padx=20, pady=20)
frame.pack(expand=True)

text_label = Label(frame, text="Doraemon Assistant", font=("Comic Sans MS", 14, "bold"), bg="#FA9999")
text_label.pack(pady=(0, 20))

original_img = Image.open("doraemon_cute.jpg")
resized_img = original_img.resize((250, 250), Image.LANCZOS)
image = ImageTk.PhotoImage(resized_img)

image_label = Label(frame, image=image, bg="#FAF16E")
image_label.pack(pady=(0, 20))

text = Text(frame, font=("Courier", 10, "bold"), bg="#FA9999", height=6, width=35)
text.pack()

entry = Entry(root, justify=CENTER)
entry.place(x=150, y=500, width=250, height=30)

Button(root, text="ASK", bg="#FFFFFF", pady=16, padx=40, borderwidth=3, relief=SOLID, command=ask).place(x=60, y=545)
Button(root, text="SEND", bg="#FFFFFF", pady=16, padx=40, borderwidth=3, relief=SOLID, command=send).place(x=210, y=545)
Button(root, text="DELETE", bg="#FFFFFF", pady=16, padx=40, borderwidth=3, relief=SOLID, command=del_text).place(x=360, y=545)

root.mainloop()

# speech_to_text.py
import speech_recognition as sr

def speech_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            voice_data = r.recognize_google(audio)
            print("You said:", voice_data)
            return voice_data
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
            return ""
        except sr.RequestError:
            print("RequestError: Could not request results from Google.")
            return ""

# text_to_speech.py
import pyttsx3

def text_to_speech(text):
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 70)
    engine.say(text)
    engine.runAndWait()

# action.py
import text_to_speech
import speech_to_text
import datetime
import webbrowser
import weather

def Action(user_data=None):
    if not user_data:
        user_data = speech_to_text.speech_to_text().lower()
    else:
        user_data = user_data.lower()

    if "what is your name" in user_data:
        text_to_speech.text_to_speech("My name is Doraemon Assistant")
        return "My name is Doraemon Assistant"

    elif "hello" in user_data or "hye" in user_data:
        text_to_speech.text_to_speech("Hey sir, how can I help you")
        return "Hey sir, how can I help you!"

    elif "good morning" in user_data:
        text_to_speech.text_to_speech("Good morning sir")
        return "Good morning sir"

    elif "time now" in user_data:
        current_time = datetime.datetime.now()
        time_text = f"It is {current_time.hour} hour and {current_time.minute} minute"
        text_to_speech.text_to_speech(time_text)
        return time_text

    elif "shutdown" in user_data:
        text_to_speech.text_to_speech("Okay sir")
        return "ok sir"

    elif "play music" in user_data:
        webbrowser.open("https://spotify.com")
        text_to_speech.text_to_speech("Spotify is now ready for you")
        return "Spotify is now ready for you"

    elif "youtube" in user_data:
        webbrowser.open("https://www.youtube.com/")
        text_to_speech.text_to_speech("YouTube is now ready for you")
        return "YouTube is now ready for you"

    elif "google" in user_data:
        webbrowser.open("https://www.google.com/")
        text_to_speech.text_to_speech("Google is now ready for you")
        return "Google is now ready for you"

    elif "weather" in user_data:
        ans = weather.weather()
        text_to_speech.text_to_speech(ans)
        return ans

    else:
        text_to_speech.text_to_speech("I am not able to understand")
        return "I am not able to understand"

# weather.py
from requests_html import HTMLSession

def weather():
    s = HTMLSession()
    query = "patna"
    url = f'https://www.google.com/search?q=weather+{query}'
    r = s.get(url, headers={'User-Agent': 'Mozilla/5.0'})

    temp = r.html.find('span#wob_tm', first=True).text
    unit = r.html.find('div.vk_bk.wob-unit span.wob_t', first=True).text
    desc = r.html.find('span#wob_dc', first=True).text
    return temp + " " + unit + " " + desc

root.mainloop()