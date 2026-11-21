def caesar(text, shift, encrypt=True):

    if not isinstance(shift, int) or isinstance(shift, bool):
        return 'Shift must be an integer value.'

    if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25.'

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    if not encrypt:
        shift = - shift
    
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    return text.translate(translation_table)

def encrypt(text, shift):
    return caesar(text, shift)
    
def decrypt(text, shift):
    return caesar(text, shift, encrypt=False)

def main():
    print("=== Caesar Cipher ===")

    choice = input("Type 'e' to encrypt or 'd' to decrypt: ").strip().lower()
    if choice not in ('e', 'd'):
        print("Invalid choice. Please type 'e' or 'd'.")
        return

    user_text = input("Enter your text: ")

    shift_input = input("Enter shift (1-25): ").strip()
    try:
        shift_value = int(shift_input)
    except ValueError:
        print('Shift must be an integer value.')
        return

    if choice == 'e':
        result = encrypt(user_text, shift_value)
    else:
        result = decrypt(user_text, shift_value)

    print("Result:", result)

main()
