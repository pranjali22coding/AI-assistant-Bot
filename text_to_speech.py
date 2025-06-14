import pyttsx3

def text_to_speech(text):
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 70)  # Reduce the speech rate
    engine.say(text)
    engine.runAndWait()

# Example call with actual text
text_to_speech("Hello! I am your Doremon assistant.")
