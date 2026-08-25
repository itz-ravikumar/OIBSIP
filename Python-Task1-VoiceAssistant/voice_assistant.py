import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import psutil
import pyautogui
import keyboard
# pyrefly: ignore [missing-import]
import wikipedia
from AppOpener import open as appopen

# Initialize the text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 160)

def speak(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
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

def main():
    speak("Hello! I am your advanced voice assistant. How can I help you today?")
    
    while True:
        command = listen()
        if not command:
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
            confirmation = listen()
            if confirmation and "yes" in confirmation:
                speak("Restarting the computer.")
                os.system("shutdown /r /t 5")
            else:
                speak("Restart cancelled.")
                
        elif "shut down the computer" in command or "shutdown" in command:
            speak("Are you sure you want to shut down? Say yes to confirm.")
            confirmation = listen()
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
