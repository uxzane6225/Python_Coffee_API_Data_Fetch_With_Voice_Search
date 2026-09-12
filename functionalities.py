import requests
from dotenv import load_dotenv
import speech_funky as sf

load_dotenv()

import os
base_url = os.getenv('BASE_URL')


def get_coffee(name):
    try:
        url = f"{base_url}?title={name}"
        response = requests.get(url)
        # print(response)
        return response
    except ConnectionError:
        print("Connection Error")
    except Exception as e:
        print(e)

def handle_response(response):
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to retrieve data {response.status_code}")

def look_menu():
    url = base_url
    response = requests.get(url)
    return response

def get_input():
    inputType = input("Type or voice? (t/v): ")
    coffee = ""
    isInputting = True

    while isInputting:
        if inputType == "t" or inputType == "T":
            coffee = input("Enter a Coffee: ")
        elif inputType == "v" or inputType == "V":
            coffee = sf.getCoffee()
        else:
            print("again")

        # print("After inputting: " + coffee)
        response = get_coffee(coffee)
        data = handle_response(response)
        
        if data:
            isInputting = False
        elif coffee == "Exit":
            print("exiting...")
            isInputting = False
            run = False
        else:
            print(f"{coffee} is not a valid product! Try again.")

    return data