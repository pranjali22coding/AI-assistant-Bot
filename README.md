# AI-assistant-Bot
A friendly desktop voice assistant powered by Python that responds to your voice or text commands! Inspired by the popular cartoon character Doraemon, this assistant can greet you, tell the time, open websites, fetch current weather, and more- all through a fun and colorful graphical interface.
Features
🎙️ Speech-to-Text input using Google's Speech Recognition

🔊 Text-to-Speech responses via pyttsx3

🧠 Command handling and logic for weather, greetings, time, shutdown, and opening websites like YouTube, Google, Spotify

🌦️ Real-time weather updates via scraping Google Weather

🖥️ Tkinter-based GUI with Doraemon theme

📥 Text-based input and buttons for flexibility

Project Structure
📦 Doraemon-Assistant
├── GUI.py               # Main GUI interface with buttons and chat display
├── main_gui.py          # Alternate GUI entry point
├── speech_to_text.py    # Captures and converts audio input to text
├── text_to_speech.py    # Converts responses to audible speech
├── action.py            # Core logic to parse commands and trigger responses
├── weather.py           # Fetches live weather information
└── doraemon_cute.jpg    # Optional GUI image (Doraemon)
Requirements
pip install speechrecognition pyttsx3 requests-html pillow
How to Run
python GUI.py
 Notes
Speech input uses the Google Web Speech API.

Weather data is scraped directly from Google search results for Patna. You can change the city in weather.py.

Ensure microphone permissions are granted.
