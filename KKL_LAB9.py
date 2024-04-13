def encode(password):
    encoded_password = ""
    for char in password:
        if char in ["7", "8", "9"]:
            encoded_char = str(int(char) + 3)[1]
            encoded_password += encoded_char
        else:
            encoded_char = int(char) + 3
            encoded_password += str(encoded_char)
    return encoded_password


def print_menu():
    print("""\nMenu
-------------
1. Encode
2. Decode
3. Quit\n""")


def main():
    encoded_password = None
    while True:
        print_menu()
        choice = int(input("Please enter an option: "))
        if choice == 1:
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
            print("Your password has been encoded and stored!")
        elif choice == 2:
            if encoded_password:
                original_password = decode(encoded_password)
                print("The encoded password is {}, and the original password is {}.".format(encoded_password, original_password))
            else:
                print("No password has been encoded yet.")
        elif choice == 3:
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
