import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import requests
import camera
import webbrowser
import news
import email
import gmail
import imaplib

def query_gpt(prompt):
    url = "https://api.openai.com/v1/completions"
    payload = {
        "model": "text-davinci-003",  # You can use different models based on your preferences
        "prompt": prompt,
        "api_key": "sk-proj-pHgsMStVXUosKp3SPosAT3BlbkFJwJJG33g9ebiYyQbCfT2P"  # Replace "YOUR_API_KEY" with your actual API key
    }
    headers = {
        "Content-Type": "application/json",
    }
    response = requests.post(url, json=payload, headers=headers)
    try:
        data = response.json()
        text = data['choices'][0]['text']
        return text
    except KeyError:
        print("Error: Unexpected response format from GPT-3 API")
        return None
    except Exception as e:
        print("Error:", e)
        return None

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
                return command  # Returning the command inside the 'if' block
    except:
        pass
    return ""  # Return an empty string if no command is recognized
def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        print('song:', song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M:%S:%p:%a')
        print(time)
        talk('Current time is' + time)

    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif 'are you single' in command:
        talk('I am in a relationship with wifi. I am sorry I am already committed to wifi.')
        talk('Maybe I can find you a date, thats if you want.')

    elif 'joke' in command:
        talk(pyjokes.get_joke())

    elif 'access camera' in command:  # If the command mentions 'camera'
        talk('Accessing camera')  # Provide feedback to the user
        camera.access_camera()  # Call the access_camera function from camera.py


    elif 'morning' in command:
        talk('Good morning Father.I hope you had a good night.')

    elif 'open gmail' in command:
        webbrowser.open_new_tab("gmail.com")
        talk("Google gmail opening now")

    elif 'read news' in command:  # If the command mentions 'read news'
        talk('Fetching latest news')  # Provide feedback to the user
        news_prompt = "Fetch me the latest news"  # Create a prompt for the GPT-3 model
        news_text = news.get_trending_news( "eb3c79c6efed4785b2cfcb1b2bc351e2")  # Use the query_gpt function from news.py to fetch news
        if news_text:  # If news text is successfully retrieved
            talk(news_text)  # Read out the news
        else:
            talk("Sorry, I couldn't fetch the news at the moment.")
run_alexa()



