import speech_recognition as sr
r = sr.Recognizer()

def store_text(input):
    try:
        f = open('output.txt', 'a')
        f.write(input)
        f.write("\n")
    except Exception as e:
        print(e)
    finally:
        f.close()


def capitalizing(input):
    toWords = input.split()
    newInput = ""

    for word in toWords:
        capitalized = word.capitalize()
        newInput += f"{capitalized} "

    return newInput

def getCoffee():
    isGettingCoffee = True
    while isGettingCoffee:
        try:
            with sr.Microphone() as source:
                print("Listening...")

                r.adjust_for_ambient_noise(source, duration=0.2)
                audio = r.listen(source)
                text = r.recognize_google(audio)
                # text = text.lower()
                # print("You said:", text)
                
                store_text(text)

                newText = capitalizing(text)

                print("You said: " + newText)

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