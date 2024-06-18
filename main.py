def caesar_cipher(text: str, shift: int) -> str:
    """
    Encrypt or decrypt a given text using the Caesar cipher technique.

    Args:
        text (str): The text to be encrypted or decrypted.
        shift (int): The shift value for the Caesar cipher.

    Returns:
        str: The resulting encrypted or decrypted text.
    """
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            base = ord('a') if char.islower() else ord('A')
            encrypted_char = chr(((ord(char) - base + shift) % 26) + base)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char  # Leave non-letter characters unchanged
    return encrypted_text


def get_valid_shift() -> int:
    """
    Get a valid shift value from the user.

    Returns:
        int: A valid shift value between -25 and 25.
    """
    while True:
        try:
            shift = int(input("Enter shift value (a number between -25 and 25): "))
            if -25 <= shift <= 25:
                return shift
            else:
                print("Invalid input. Please enter a number between -25 and 25.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def main():
    """
    The main function to run the Caesar cipher program.
    """
    message = input("Enter message: ")
    shift = get_valid_shift()

    encrypted_message = caesar_cipher(message, shift)
    print("Encrypted message:", encrypted_message)

    decrypted_message = caesar_cipher(encrypted_message, -shift)
    print("Decrypted message:", decrypted_message)


if __name__ == "__main__":
    main()
