number_dict = {}

# декоратор який обробляє помилки при вводі з консолі
def input_error(handler):
    def wrapper(*args, **kwargs):
        try:
            return handler(*args, **kwargs)
        except KeyError:
            return "Enter user name"
        except ValueError:
            return "Give me name and phone please"
        except IndexError:
            return "Invalid index"
    return wrapper


# функція яка виконується при команді "hello"
@input_error
def greeting():
    return "How can I help you?"


# зберігає у словник новий контакт(ім'я і номер)
@input_error
def add_contact(data):
    _, name, number = data.split()
    number_dict.update({name: number})
    return "Contact added successfully"


# міняє номер уже існуючого контакта 
@input_error
def change_phone_number(data):
    _, name, number = data.split()
    number_dict[name] = number
    return "Phone number updated"


# виводиться у консоль номер вказаного контакту 
@input_error
def contact_number(data):
    _, name = data.split()
    if name in number_dict:
        return f"Phone number for {name}: {number_dict[name]}"
    else:
        return f"Contact {name} not found"


# вивід всіх збережених контактів(ім'я і номер)
def show_all_number():
    if number_dict:
        result = ""
        for name, phone in number_dict.items():
            result += f"{name}: {phone}\n"
        return result.strip()
    else:
        return "No contacts found"


# основна функція, яка приймає команди і за допомогою інших функцій обробляє їх
# вихід з циклу можливий тільки тоді, коли буде введена ключова команда
def main():
    while True:
        user_input = input("Enter a command: ").lower()

        if user_input in ["good bye", "close", "exit"]:
            print("Good bye!")
            break

        if user_input == "hello":
            print(greeting())

        elif user_input.startswith("add"):
            print(add_contact(user_input))

        elif user_input.startswith("change"):
            print(change_phone_number(user_input))

        elif user_input.startswith("phone"):
            print(contact_number(user_input))

        elif user_input == "show all":
            print(show_all_number())

        else:
            print("Unknown command. Please try again.")

# виклик функції при запуску програми            
if __name__ == '__main__':
    main()