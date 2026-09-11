import requests
import speech_recognition as sr
from dotenv import load_dotenv
load_dotenv()

import os
base_url = os.getenv('BASE_URL')
r = sr.Recognizer()

def get_coffee(name):
    url = f"{base_url}?title={name}"
    response = requests.get(url)
    # print(response)
    return response

def handle_response(response):
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to retrieve data {response.status_code}")

def look_menu():
    url = base_url
    response = requests.get(url)
    return response


def getCoffee():
    isGettingCoffee = True
    while isGettingCoffee:
        try:
            with sr.Microphone() as source:
                print("Listening...")

                r.adjust_for_ambient_noise(source, duration=0.2)
                audio = r.listen(source)
                text = r.recognize_google(audio)
                text = text.lower()
                print("You said:", text)

                f = open('output.txt', 'a')
                f.write(text)
                f.write("\n")
                f.close()

                toWords = text.split()
                newText = ""

                for word in toWords:
                    capitalized = word.capitalize()
                    newText += f"{capitalized} "

                print(newText)

                if newText:
                    return newText.strip()
                elif "exit" in text:
                    print("Exiting program...")
                    isGettingCoffee = False

        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))

        except sr.UnknownValueError:
            print("Could not understand audio")

        except KeyboardInterrupt:
            print("Program terminated by user")
            isGettingCoffee = False