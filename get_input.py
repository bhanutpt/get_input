

def get_input_characters():
    return input("Enter characters: ")

def get_input_number():
    while True:
        chars = input("Enter a number: ")
        if is_number(chars):
            return chars
        else:
            if is_float(chars):
                print(f"Invalid input, {chars} is a floating point number, only whole numbers are valid.")
            else:
                print(f"Invalid input, {chars} is not a number.")

def get_input_number_binary():
    while True:
        chars = input("Enter a binary number: ")
        if is_number_binary(chars):
            return chars
        else:
            print(f"Invalid input, {chars} is not a binary number.")

def get_input_number_hex():
    while True:
        chars = input("Enter a hexadecimal number: ")
        if is_number_hex(chars):
            return chars
        else:
            print(f"Invalid input, {chars} is not a hexadecimal number.")

def get_input_number_oct():
    while True:
        chars = input("Enter an octal number: ")
        if is_number_oct(chars):
            return chars
        else:
            print(f"Invalid input, {chars} is not an octal number.")

def get_input_digit():
    while True:
        chars = input("Enter a digit: ")
        if is_digit(chars):
            return chars
        else:
            print(f"Invalid input, {chars} is not a single digit.")

def get_input_digit_binary():
    while True:
        chars = input("Enter a binary digit: ")
        if is_digit_binary(chars):
            return chars
        else:
            print(f"Invalid input, {chars} is not a binary digit.")

def get_input_digit_hex():
    while True:
        chars = input("Enter a hexadecimal digit: ")
        if is_digit_hex(chars):
            return chars
        else:
            print(f"Invalid input, {chars} is not a hexadecimal digit.")

def get_input_digit_oct():
    while True:
        chars = input("Enter an octal digit: ")
        if is_digit_oct(chars):
            return chars
        else:
            print(f"Invalid input, {chars} is not an octal digit.")

def is_number(value):
    return value.isdigit()

def is_number_binary(value):
    return all(char in '01' for char in value)

def is_number_hex(value):
    return all(char in '0123456789ABCDEFabcdef' for char in value)

def is_number_oct(value):
    return all(char in '01234567' for char in value)

def is_digit(value):
    return value.isdigit() and len(value) == 1

def is_digit_binary(value):
    return value in '01' and len(value) == 1

def is_digit_hex(value):
    return value in '0123456789ABCDEFabcdef' and len(value) == 1

def is_digit_oct(value):
    return value in '01234567' and len(value) == 1

def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

# Example usage
if __name__ == "__main__":
    print(get_input_characters())
    print(get_input_number())
    print(get_input_number_binary())
    print(get_input_number_hex())
    print(get_input_number_oct())
    print(get_input_digit())
    print(get_input_digit_binary())
    print(get_input_digit_hex())
    print(get_input_digit_oct())

    print(is_number("123"))
    print(is_number_binary("1010"))
    print(is_number_hex("1A2B"))
    print(is_number_oct("567"))

    print(is_digit("5"))
    print(is_digit_binary("1"))
    print(is_digit_hex("A"))
    print(is_digit_oct("7"))
    print(is_float("123.123"))

