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
