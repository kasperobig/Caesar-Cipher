import string

# Ask to enter the plaintext
plaintext = input("Your text: ")

# Ask key code
key = input("Secret code:")

# Ask for choice Encrypting or Decrypting
is_encrypt = input("1- Encrypting \n 2- Decrypting \n What is your choice: ")

if is_encrypt == "2":
    key = 26 - int(key)


def Caesar(input_text, key):
    ciphertext = ""

    input_text = plaintext.lower()
    for c in input_text:
        if c in string.ascii_letters:
            temp = ord(c) + int(key)

            if temp > ord("z"):
                temp = temp - 26

            ciphertext = ciphertext + chr(temp)

        else:
            ciphertext = ciphertext + c

    return ciphertext


print(Caesar(plaintext, key))
