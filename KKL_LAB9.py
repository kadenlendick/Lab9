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