import time
import random
import datetime
import os
import speech_recognition as sr
import pyttsx3
import google.generativeai as genai
from decouple import config

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Set properties for the TTS engine (optional)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 180)  # Speed of speech
engine.setProperty('volume', 1)   # Volume level (0.0 to 1.0)

# Configure Google Generative AI (Gemini)
GOOGLE_API_KEY = 'AIzaSyBWbSfAZik6N_NP4bGXf9_w9T03Nuf_SJE'
genai.configure(api_key=GOOGLE_API_KEY)

# Generation configuration
generation_config = {
    "temperature": 0.7,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048
}

# Safety settings
safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"}
]

# Initialize the model
model = genai.GenerativeModel('gemini-1.0-pro-latest', generation_config=generation_config, safety_settings=safety_settings)

# Function to speak out the text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen to the user's voice input
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print(f"User said: {query}")
        return query
    except sr.UnknownValueError:
        speak("Sorry, I did not understand that. Could you repeat?")
        return None
    except sr.RequestError:
        speak("Sorry, there was an issue with the voice recognition service.")
        return None

# Main function to handle the assistant's logic
def voice_assistant():
    speak("Hello! How can I assist you today?")
    
    while True:
        # Listen for a query from the user
        query = listen()
        if query is None:
            continue

        # Check for predefined responses
    
def find_room_number(x):
    room = ["aiml", "cse", "vc", "hod", "engineering staff room", "computer lab", "library", "registard"]
    room_numbers = [207, 206, 105, 201, 202, 203, 208, 199]

    x_lower = x.lower()

    for room, room_number in zip(room, room_numbers):
        if room in x_lower:
            return f"It is on the second floor. Room number {room_number}"

    speak("Room not found.")
    return "Room not found."        

# Main function to handle the assistant's logic
def voice_assistant():
    speak("Hello! This is Check-Mate i am here to smoothen your checkin process.")
    speak("What is your name?")
    print("Listening")
    time.sleep(5.5)
    speak("tell me your address")
    time.sleep(5.5)
    speak("tell me the purpose of the visit")
    time.sleep(5.5)
    speak("How can i help you?")


    while True:
        # Listen for a query from the user
        query = listen()
        if query is None:
            continue

        # Check for predefined responses
        if 'creator' in query.lower():
            response = "I am developed by Shyamji Pandey and his dedicated team, in partnership with esteemed researchers at Amity University, Bengaluru."
            print(f"Gemini AI response: {response}")
            speak(response)
            continue
        elif 'campus' in query.lower():
            response = "Amity University Bangalore has a vibrant campus with modern facilities and a supportive community."
            print(f"Gemini AI response: {response}")
            speak(response)
            continue

        # Additional conditions
        elif "the time" in query.lower():
            strfTime = datetime.datetime.now().strftime("%H:%M:%S")
            response = f"The time is {strfTime}."
            print(f"Gemini AI response: {response}")
            speak(response)
            continue
        elif "quit" in query.lower():
            response = "Goodbye."
            print(f"Gemini AI response: {response}")
            speak(response)
            exit()
        elif "birthday" in query.lower():
            response = ("As an artificial intelligence, I don't have a birthday like humans. However, I was created on the second of February 2024 by the team Roboverse.")
            print(f"Gemini AI response: {response}")
            speak(response)
            continue
        elif "shutdown" in query.lower():
            response = "Shutting down."
            print(f"Gemini AI response: {response}")
            speak(response)
            os.system("shutdown /s /t 1")
        elif any(room in query.lower() for room in ["aiml", "cse", "vc", "hod", "engineering staff room", "computer lab", "library", "registrar"]):
            room_info = find_room_number(query)
            print(f"Gemini AI response: {room_info}")
            speak(room_info)
            continue
        elif "thank you" in query.lower():
            response = "You're most welcome! Have a nice day. Goodbye..."
            print(f"Gemini AI response: {response}")
            speak(response)
            exit()
        elif "chancellor" in query.lower():
            response = "The Chancellor for Amity University Bengaluru is Aseem Chauhan."
            print(f"Gemini AI response: {response}")
            speak(response)
            continue
        elif "vice chancellor" in query.lower():
            response = "The Vice Chancellor for Amity University Bengaluru is Dr. Sudhakar."
            print(f"Gemini AI response: {response}")
            speak(response)
            continue
        elif "president" in query.lower():
            response = "The President for Amity University Bengaluru is Dr. P sali."
            print(f"Gemini AI response: {response}")
            speak(response)# Process query using Google Generative AI (Gemini)
            continue
        convo = model.start_chat()
        
        # Prepare the system message
        system_message = "You are being used to power a humanoid receptionist robot at Amity University Bangalore. Your name is Check-Mate. Use short sentences and directly respond to the prompt without excessive information. While answering, do not use asterisks."
        convo.send_message(system_message)
        
        # Send user input to the model
        convo.send_message(query)

        # Get the AI's response
        response = convo.last.text
        print(f"Gemini AI response: {response}")

        # Speak the response back to the user
        speak(response)

        # Exit if the user says 'exit'
        if 'thank' in query.lower():
            speak("Goodbye!")
            break

if __name__ == '__main__':
    voice_assistant()





























