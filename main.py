import pyperclip


INTRO = """
Welcome to...
 _  _   __  ____  _  _     ___  __  ____  ____ 
( \/ ) /  \(  _ \( \/ )   / __)/  \(    \(  __)
/ \/ \(  O )) __/ )  /   ( (__(  O )) D ( ) _) 
\_)(_/ \__/(__)  (__/     \___)\__/(____/(____)
The Morse Code Converter
"""

# Define the Morse code dictionary
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', 
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    ', ': '--..--', '.': '.-.-.-', '?': '..--..', "'": '.----.', '!': '-.-.--',
    '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...',
    ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-',
    '"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ': '/'
}
def text_to_morse(text: str) -> str:
    """
    Convert the input text to Morse code.
    """
    # Convert the input text to uppercase
    text = text.upper()

    # Initialize an empty string for the Morse code
    morse_code = ''

    # Translate each character in the text to Morse code
    for char in text:
        if char in MORSE_CODE_DICT:
            morse_code += MORSE_CODE_DICT[char] + ' '
        else:
            morse_code += ' '

    return morse_code.strip()

# Main function to get user input and convert it to Morse code
if __name__ == "__main__":
    print(INTRO)
    print("Enter the text you want to convert to Morse code.")

    while True:
        # Get the input text from the user
        input_text = input("Enter the text to convert to Morse code (or 'q' to quit): ")

        # Check if the user wants to quit
        if input_text.lower() == 'q':
            print("Exiting the program.")
            break

        # Convert the input text to Morse code
        morse_code = text_to_morse(input_text)
        
        pyperclip.copy(morse_code)

        # Display the Morse code
        print("Morse Code:", morse_code)
        print('(Copied to clipboard)\n')
