def load_morse_code():
    morse_dict = {}
    with open('abc.txt', 'r') as file:
        for line in file:
            if line.strip():
                parts = line.strip().split(' ', 1)
                if len(parts) == 2:
                    character, morse = parts
                    morse_dict[character] = morse
                else:

                    print(f"Issue with line: {line.strip()}. Skipping.")
    return morse_dict

def text_to_morse(text, morse_dict):
    morse_result = []
    for char in text.upper():
        if char in morse_dict:
            morse_result.append(morse_dict[char])
        else:
            morse_result.append(' ')
    return ' '.join(morse_result)

# Loading Morse code mappings
morse_mapping = load_morse_code()

# Getting user input and translating it to Morse code
user_input = input("Preloz: ")
morse_output = text_to_morse(user_input, morse_mapping)
print("Morse code:", morse_output)
