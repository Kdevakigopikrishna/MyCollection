# task-1
# what will u say it printit and if issue try this install:-pip install SpeechRecognition and also pip install PyAudio.

import speech_recognition as sr

# Initialize recognizer
recognizer = sr.Recognizer()

# Use the microphone as a source for input
with sr.Microphone() as source:
    print("Say something:")
    audio = recognizer.listen(source)

# Recognize speech using Google Web Speech API
try:
    print("You said: " + recognizer.recognize_google(audio))
except sr.UnknownValueError:
    print("Could not understand the audio")
except sr.RequestError:
    print("Could not request results; check your internet connection")









#task 2
#let here if  u ask any question it will provied u just links or websites etc... but not provied what is what!
#and if issue try this install:-pip install googlesearch-python


import speech_recognition as sr
from googlesearch import search

# Initialize recognizer
recognizer = sr.Recognizer()

# Use the microphone as a source for input
with sr.Microphone() as source:
    print("Listening for your search query...")
    audio = recognizer.listen(source)

try:
    # Recognize the voice input
    command = recognizer.recognize_google(audio)
    print(f"You said: {command}")

    # Perform a Google search using the voice command as the query
    print(f"Searching Google for: {command}")
    search_results = search(command, num_results=5)
    
    # Print the top 5 search results
    print("Here are the top results:")
    for index, result in enumerate(search_results, start=1):
        print(f"Result {index}: {result}")
    
except sr.UnknownValueError:
    print("Could not understand the audio.")
except sr.RequestError:
    print("Could not request results; check your internet connection.")




#task 3

#let here will u get the ,if u ask a question it wiil give u a summary or what is what and it may be 
 # give the links also ect....
  #and if an issue tyr this :-pip install beautifulsoup4 requests

import speech_recognition as sr
from googlesearch import search
import requests
from bs4 import BeautifulSoup

# Function to extract content from the first search result
def extract_content_from_url(url):
    try:
        # Fetch the web page
        response = requests.get(url)
        if response.status_code == 200:
            # Parse the content with BeautifulSoup
            soup = BeautifulSoup(response.content, 'html.parser')
            # Extract text from the page (you can refine this to get specific parts like paragraphs, headers, etc.)
            paragraphs = soup.find_all('p')
            content = ' '.join([para.get_text() for para in paragraphs[:5]])  # Get first 5 paragraphs as a summary
            return content
        else:
            return "Could not retrieve content from the webpage."
    except Exception as e:
        return str(e)

# Initialize recognizer
recognizer = sr.Recognizer()

# Use the microphone as a source for input
with sr.Microphone() as source:
    print("Listening for your search query...")
    audio = recognizer.listen(source)
try:
    # Recognize the voice input
    command = recognizer.recognize_google(audio)
    print(f"You said: {command}")

    # Perform a Google search using the voice command as the query
    print(f"Searching Google for: {command}")
    search_results = search(command, num_results=1)  # Limit to the top result

    # Process the first search result
    first_result_url = next(search_results)
    print(f"Top result: {first_result_url}")
    
    # Extract content from the top result
    content = extract_content_from_url(first_result_url)
    print("\nHere is the extracted information:")
    print(content)
except sr.UnknownValueError:
    print("Could not understand the audio.")
except sr.RequestError:
    print("Could not request results; check your internet connection.")
except Exception as e:
    print(f"An error occurred: {e}")




#task 4
#what every u  will enter it will speak:-pip install pyttsx3,  pip install SpeechRecognition pyttsx3 pyaudio

import pyttsx3
# Initialize the text-to-speech engine
engine = pyttsx3.init()
# Get user input
message = input("Enter a message: ")
# Make the engine say the message
engine.say(message)
# Run the speech engine
engine.runAndWait()



