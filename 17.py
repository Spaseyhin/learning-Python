def filter_string(line: str, letter: str) -> str:
    result = ''
    for current_char in line:
        if current_char.lower() != letter.lower():
            result += current_char
    return result 

print(filter_string("hello world", "O")) # Output: hell wrld