import requests

base_url = "https://api.sampleapis.com/coffee/hot"

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
while True:
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
                break

        coffee = input("Enter a Coffee: ")

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
        break
    except ConnectionError:
        print("No connection was made")
        break
    finally:
        print("The end")
        break