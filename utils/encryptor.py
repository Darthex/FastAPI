def encrypt(message, key):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            # Shift the character by the key value
            encrypted_char = chr((ord(char) + key - ord('a')) % 26 + ord('a')) if char.islower() else chr(
                (ord(char) + key - ord('A')) % 26 + ord('A'))
            encrypted_message += encrypted_char
        else:
            # Leave non-alphabetic characters unchanged
            encrypted_message += char
    return encrypted_message


def decrypt(message, key):
    return encrypt(message, -key)
