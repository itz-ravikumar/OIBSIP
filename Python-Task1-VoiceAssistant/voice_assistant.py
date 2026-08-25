import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import psutil
import pyautogui
import keyboard
import wikipedia
import smtplib
from email.message import EmailMessage
import threading
import winsound
import requests
import json
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
from AppOpener import open as appopen

# Make sure nltk data is available
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt', quiet=True)
try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords', quiet=True)

# Initialize the text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 160)

def speak(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

def listen(timeout=5, phrase_time_limit=10):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        try:
            audio = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
            print("Recognizing...")
            command = recognizer.recognize_google(audio).lower()
            print(f"You said: {command}")
            return command
        except sr.UnknownValueError:
            speak("Sorry, I didn't quite catch that. Could you please repeat?")
            return None
        except sr.RequestError as e:
            speak("There seems to be an issue with the speech recognition service.")
            return None
        except sr.WaitTimeoutError:
            return None

def trigger_reminder(message):
    print(f"\n[REMINDER ALERT] {message}")
    winsound.Beep(1000, 1000) # Beep for 1 second

def parse_intent(text):
    """Basic NLU Intent Parsing using NLTK."""
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [w for w in tokens if not w in stop_words and w not in string.punctuation]
    
    if "email" in filtered_tokens or ("send" in filtered_tokens and "mail" in filtered_tokens): return "email"
    if "weather" in filtered_tokens or "temperature" in filtered_tokens: return "weather"
    if "remind" in filtered_tokens or "reminder" in filtered_tokens: return "reminder"
    
    return None

def load_custom_commands():
    try:
        if os.path.exists("commands.json"):
            with open("commands.json", "r") as f:
                return json.load(f)
    except Exception as e:
        print(f"Error loading commands.json: {e}")
    return {}

def main():
    speak("Hello! I am your advanced voice assistant. How can I help you today?")
    custom_commands = load_custom_commands()

    while True:
        command = listen()
        if not command:
            continue
            
        # Check Custom Commands First
        matched_custom = False
        for trigger, response in custom_commands.items():
            if trigger in command:
                speak(response)
                matched_custom = True
                break
        if matched_custom:
            continue

        # NLU Intent Parsing for Advanced Features
        intent = parse_intent(command)
        
        if intent == "email":
            speak("Who is the recipient?")
            recipient = listen(phrase_time_limit=5)
            if not recipient: continue
            
            speak("What is the subject?")
            subject = listen(phrase_time_limit=5)
            if not subject: continue
            
            speak("What is the message?")
            body = listen(phrase_time_limit=15)
            if not body: continue
            
            # Dummy credentials
            EMAIL_ADDRESS = os.environ.get("EMAIL_USER", "dummy_test_assistant_123@gmail.com")
            EMAIL_PASSWORD = os.environ.get("EMAIL_PASS", "dummy_app_password")
            
            if EMAIL_PASSWORD == "dummy_app_password":
                speak("I need a real email and app password set in the environment variables to actually send it, but I've drafted it successfully.")
                print(f"Draft:\nTo: {recipient}\nSubject: {subject}\nBody: {body}")
            else:
                try:
                    msg = EmailMessage()
                    msg['Subject'] = subject
                    msg['From'] = EMAIL_ADDRESS
                    msg['To'] = recipient
                    msg.set_content(body)
                    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                        smtp.send_message(msg)
                    speak("Email sent successfully.")
                except Exception as e:
                    speak("Failed to send email.")
                    print(e)
            continue
            
        elif intent == "weather":
            # Very basic extraction for demo purposes
            city = "London"
            words = command.split()
            if "in" in words:
                idx = words.index("in")
                if idx + 1 < len(words):
                    city = words[idx + 1]
            speak(f"Fetching weather for {city}...")
            try:
                # wttr.in gives plain text weather format 3 gives location and temp
                res = requests.get(f"https://wttr.in/{city}?format=3", timeout=5)
                if res.status_code == 200:
                    speak(res.text.strip())
                else:
                    speak("I couldn't fetch the weather right now.")
            except:
                speak("I couldn't fetch the weather right now.")
            continue
            
        elif intent == "reminder":
            speak("What should I remind you about?")
            message = listen()
            if not message: continue
            
            speak("In how many seconds should I remind you? Please say a number.")
            duration_str = listen(phrase_time_limit=5)
            if not duration_str: continue
            
            try:
                # Basic extraction of number from voice
                numbers = [int(s) for s in duration_str.split() if s.isdigit()]
                duration = numbers[0] if numbers else 10 # default 10s
                
                t = threading.Timer(duration, trigger_reminder, args=[message])
                t.start()
                speak(f"Reminder set for {duration} seconds.")
            except Exception as e:
                speak("Sorry, I didn't understand the duration. Reminder not set.")
            continue

        # Basic Interactions
        if "hello" in command or "hi" in command:
            speak("Hello there! How can I assist you today?")
            
        elif "time" in command:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The current time is {current_time}.")
            
        elif "date" in command:
            current_date = datetime.datetime.now().strftime("%B %d, %Y")
            speak(f"Today's date is {current_date}.")
            
        # Knowledge Search (Wikipedia)
        elif "wikipedia" in command or "who is" in command or "what is" in command:
            query = command.replace("wikipedia", "").replace("who is", "").replace("what is", "").strip()
            if query:
                speak(f"Searching Wikipedia for {query}...")
                try:
                    results = wikipedia.summary(query, sentences=2)
                    speak("According to Wikipedia:")
                    speak(results)
                except wikipedia.exceptions.DisambiguationError:
                    speak(f"There are multiple results for {query}. Please be more specific.")
                except wikipedia.exceptions.PageError:
                    speak(f"I couldn't find anything about {query} on Wikipedia.")
                except Exception:
                    speak("An error occurred while searching Wikipedia.")
            else:
                speak("What do you want me to search on Wikipedia?")

        # Web Search (Google)
        elif "search" in command:
            query = command.replace("search", "").replace("for", "").strip()
            if query:
                speak(f"Searching for {query}")
                webbrowser.open(f"https://www.google.com/search?q={query}")
            else:
                speak("What would you like me to search for?")
                
        # Media / Volume Controls
        elif "volume up" in command or "increase volume" in command:
            speak("Increasing volume.")
            for _ in range(5): keyboard.send("volume up")
            
        elif "volume down" in command or "decrease volume" in command:
            speak("Decreasing volume.")
            for _ in range(5): keyboard.send("volume down")
            
        elif "mute" in command or "unmute" in command:
            speak("Toggling mute.")
            keyboard.send("volume mute")

        # System Utilities
        elif "battery" in command:
            battery = psutil.sensors_battery()
            if battery:
                plugged = "plugged in" if battery.power_plugged else "not plugged in"
                speak(f"Your battery is at {battery.percent}% and is {plugged}.")
            else:
                speak("Sorry, I cannot detect the battery status.")
                
        elif "screenshot" in command:
            speak("Taking a screenshot...")
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"screenshot_{timestamp}.png"
            path = os.path.join(os.path.expanduser('~'), 'Desktop', filename)
            try:
                pyautogui.screenshot(path)
                speak(f"Screenshot saved to your Desktop as {filename}.")
            except Exception as e:
                speak("I couldn't take a screenshot. This might be due to missing display permissions.")
                print(f"Screenshot error: {e}")

        # Power Controls
        elif "lock the computer" in command or "lock my pc" in command:
            speak("Locking the computer.")
            os.system("rundll32.exe user32.dll,LockWorkStation")
            
        elif "sleep" in command and "computer" in command:
            speak("Putting the computer to sleep.")
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
            
        elif "restart the computer" in command:
            speak("Are you sure you want to restart? Say yes to confirm.")
            confirmation = listen(phrase_time_limit=5)
            if confirmation and "yes" in confirmation:
                speak("Restarting the computer.")
                os.system("shutdown /r /t 5")
            else:
                speak("Restart cancelled.")
                
        elif "shut down the computer" in command or "shutdown" in command:
            speak("Are you sure you want to shut down? Say yes to confirm.")
            confirmation = listen(phrase_time_limit=5)
            if confirmation and "yes" in confirmation:
                speak("Shutting down the computer.")
                os.system("shutdown /s /t 5")
            else:
                speak("Shutdown cancelled.")

        # Universal App Opening
        elif "open" in command:
            app_name = command.replace("open", "").strip()
            # Handle specific websites first to prevent AppOpener from failing
            if "youtube" in app_name:
                speak("Opening YouTube")
                webbrowser.open("https://www.youtube.com")
            elif "google" in app_name:
                speak("Opening Google")
                webbrowser.open("https://www.google.com")
            elif app_name:
                speak(f"Attempting to open {app_name}")
                # AppOpener will try to find and open the app
                appopen(app_name, match_closest=True)
            else:
                speak("What would you like me to open?")

        # Exit condition
        elif "exit" in command or "quit" in command or "stop" in command:
            speak("Goodbye! Have a great day!")
            break
            
        # Fallback for unrecognized commands
        else:
            speak("I'm not sure how to help with that yet, but I'm still learning.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nAssistant: Goodbye! (Forced exit)")
