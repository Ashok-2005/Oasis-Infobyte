import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def get_audio():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio).lower()
        print("You said:", command)
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand your audio.")
        command = ""
    return command

def assistant(command):
    if "hello" in command:
        speak("Hello! How can I help you today?")

    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The current time is {current_time}")

    elif "date" in command:
        current_date = datetime.date.today().strftime("%Y-%m-%d")
        speak(f"Today's date is {current_date}")

    elif "search" in command:
        query = command.replace("search", "").strip()
        url = f"https://www.google.com/search?q={query}"
        webbrowser.open(url)
        speak(f"Here is what I found for {query} on the web.")

    else:
        speak("I'm sorry, I didn't understand that command.")

if __name__ == "__main__":
    speak("Hello! I am your voice assistant. How can I help you today?")

    while True:
        command = get_audio()
        assistant(command)
