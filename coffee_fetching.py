import requests
import speech_recognition as sr
import os
from dotenv import load_dotenv
load_dotenv()

base_url = os.getenv('BASE_URL')
print(base_url)

r = sr.Recognizer()

def get_coffee(name):
    url = f"{base_url}?title={name}"
    response = requests.get(url)
    print(response)
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

run = True
while run:
    try:
        see = input("Look at the menu? (y/n): ")
        if see == "y" or see == "Y":
            response = look_menu()
            data = handle_response(response)
            if data:
                print("--------==== LE MENU ====--------")
                print("---------------------------------")
                for coffee in data:
                    print(f"----== Coffeee #{coffee['id']} ==----")
                    print(f"Title: {coffee['title']}")
                    print(f"Description: {coffee['description']}")
                    print("--= Ingredient =--")
                    for ingredient in coffee['ingredients']:
                        print(f"- {ingredient}")
                    print("---------------------------------\n")
            else:
                run = False

        inputType = input("Type or voice? (t/v): ")
        coffee = ""
        isInputting = True
        while isInputting:
            if inputType == "t" or inputType == "T":
                coffee = input("Enter a Coffee: ")
                isInputting = False
            elif inputType == "v" or inputType == "V":
                coffee = getCoffee()
                isInputting = False
            else:
                print("again")
        print("After inputting: " + coffee)
        response = get_coffee(coffee)
        data = handle_response(response)
        # print(data)
        if data:
            print(f"ID: {data[0]['id']}")
            print(f"Title: {data[0]['title']}")
            print(f"Description: {data[0]['description']}")
            # print(f"Ingredients: {data[0]['ingredients']}")
            print("Ingredients: ")
            for ingredient in data[0]['ingredients']:
                print(f"- {ingredient}")
        else:
            raise Exception("Coffee not found!")
        run = False
    except ConnectionError:
        print("No connection was made")
        run = False
    finally:
        print("The end")
        run = False