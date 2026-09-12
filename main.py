import functionalities as funky

def main():
    run = True
    while run:
        try:
            see = input("Look at the menu? (y/n): ")

            if see == "y" or see == "Y":
                response = funky.look_menu()
                data = funky.handle_response(response)
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

            data = funky.get_input()

            # print(data)
            if data:
                print()
                print(f"ID: {data[0]['id']}")
                print(f"Title: {data[0]['title']}")
                print(f"Description: {data[0]['description']}")
                # print(f"Ingredients: {data[0]['ingredients']}")
                print("Ingredients: ")
                for ingredient in data[0]['ingredients']:
                    print(f"- {ingredient}")

            run = False
        except ConnectionError:
            print("No connection was made")
            run = False
        finally:
            print("The end")
            run = False


if __name__ == '__main__':
    main()