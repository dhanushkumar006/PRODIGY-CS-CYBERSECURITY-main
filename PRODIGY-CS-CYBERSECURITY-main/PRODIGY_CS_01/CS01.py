def encrypt(shift, message):
    result = ""
    for letter in message:
        if letter.isalpha():
            ascii_offset = 65 if letter.isupper() else 97
            result += chr((ord(letter) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += letter
    return result

def decrypt(shift, message):
    result = ""
    for letter in message:
        if letter.isalpha():
            ascii_offset = 65 if letter.isupper() else 97
            result += chr((ord(letter) - ascii_offset - shift) % 26 + ascii_offset)
        else:
            result += letter
    return result

def main():
    message = input("Enter a message: ")
    shift = int(input("Enter a shift value: "))

    encrypted = encrypt(shift, message)
    print("Encrypted message:", encrypted)

    decrypted = decrypt(shift, encrypted)
    print("Decrypted message:", decrypted)

if __name__ == "__main__":
    main()