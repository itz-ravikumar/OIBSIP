# Python-Task1-VoiceAssistant

This is a fully featured voice assistant built in Python for the OIBSIP Internship Task 1.

## Features (Beginner & Advanced Tiers)
- **Natural Language Understanding (NLU):** Uses NLTK to parse your intent dynamically.
- **Universal App Opening:** Uses `AppOpener` to open any installed application.
- **System Controls:** Lock, Sleep, Restart, Shutdown (with voice confirmation).
- **System Utilities:** Take screenshots, check battery status, control volume.
- **Web & Knowledge Search:** Google searches, Wikipedia queries.
- **Live Weather:** Fetches live weather using `wttr.in`.
- **Email Sending:** Voice-driven email drafting (requires configuration of SMTP).
- **Timed Reminders:** Background reminder alerts.
- **Custom Commands:** Easily add custom voice commands via `commands.json`.

## Privacy Considerations
- **Voice Data:** This application captures your microphone audio using the `speech_recognition` library and sends it to the **Google Web Speech API** to convert it into text. Keep in mind that audio snippets are transmitted over the internet to Google's servers.
- **Local Execution:** All other features (AppOpener, system controls, NLU intent parsing, custom commands) are processed locally on your machine.
- **Credentials:** Email sending requires an email address and an App Password. Never commit your passwords directly into the script. They should be set as Environment Variables (`EMAIL_USER` and `EMAIL_PASS`).

## How to use
Ensure all dependencies are installed via `pip`.
Run the assistant:
```bash
python voice_assistant.py
```
