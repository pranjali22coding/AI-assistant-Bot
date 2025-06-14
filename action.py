import text_to_speech
import datetime
import webbrowser
import weather

def Action(user_data):
    if not user_data:
        text_to_speech.text_to_speech("Sorry, I did not catch that.")
        return "No input detected"

    user_data = user_data.lower()

    if "what is your name" in user_data:
        text_to_speech.text_to_speech("My name is Doraemon Assistant")
        return "My name is Doraemon Assistant"

    elif "hello" in user_data or "hye" in user_data:
        text_to_speech.text_to_speech("Hey sir, how can I help you")
        return "Hey sir, how can I help you"

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

    elif "music" in user_data:
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
