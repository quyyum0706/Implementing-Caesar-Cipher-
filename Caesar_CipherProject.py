letters = 'abcdefghijklmnopqrstuvwxyz'
num_letters = len(letters)

def encrypt(plain_text, shift_key):
    cipher_text = ''
    for letter in plain_text:
        if letter.lower() in letters:
            original_case = letter.isupper()
            letter = letter.lower()
            index = letters.find(letter)
            new_index = (index + shift_key) % num_letters
            encrypted_char = letters[new_index]
            cipher_text += encrypted_char.upper() if original_case else encrypted_char
        else:
            cipher_text += letter  # Preserve non-alphabet characters and spaces
    return cipher_text

def decrypt(cipher_text, shift_key): 
    plain_text = ''
    for letter in cipher_text:
        if letter.lower() in letters:
            original_case = letter.isupper()
            letter = letter.lower()
            index = letters.find(letter)
            new_index = (index - shift_key) % num_letters
            decrypted_char = letters[new_index]
            plain_text += decrypted_char.upper() if original_case else decrypted_char
        else:
            plain_text += letter  # Preserve non-alphabet characters and spaces
    return plain_text


while True:
    print("\nCaesar Cipher Program")
    user_input = input("Press 'e' to encrypt, 'd' to decrypt, or 'q' to quit: ").lower()

    if user_input == 'q':
        print("Goodbye!")
        break

    if user_input == 'e':
        print('\nENCRYPTION MODE SELECTED')
        try:
            key = int(input('Enter the key (1 through 25): '))
            if not 1 <= key <= 25:
                print("Key must be between 1 and 25.")
                continue
            text = input('Enter the text to encrypt: ')
            cipher_text = encrypt(text, key)
            print(f'\nCIPHERTEXT: {cipher_text}')
        except ValueError:
            print("Invalid key. Please enter a number between 1 and 25.")

    elif user_input == 'd':
        print('\nDECRYPTION MODE SELECTED')
        try:
            key = int(input('Enter the key (1 through 25): '))
            if not 1 <= key <= 25:
                print("Key must be between 1 and 25.")
                continue
            text = input('Enter the text to decrypt: ')
            plain_text = decrypt(text, key)
            print(f'\nPLAINTEXT: {plain_text}')
        except ValueError:
            print("Invalid key. Please enter a number between 1 and 25.")