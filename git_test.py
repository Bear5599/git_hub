

def data(stored_value):
    if isinstance(stored_value, str):
        ascii_convert = []
        for letter in stored_value:
            letter_numbers = ord(letter)
            stored_value = ascii_convert.append(letter_numbers)
        print(ascii_convert)
        return(ascii_convert)
    else:
        return "Letters only please"
    



user_input = input("Type something: ")
data(user_input)
