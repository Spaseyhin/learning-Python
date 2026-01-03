def filter_string(line: str, letter: str) -> str:
    count_cycles = 0
    text = ''
    while count_cycles < len(line):
        if line[count_cycles].lower() != letter.lower() :
            text += line[count_cycles]
        count_cycles += 1
    return text

print(filter_string("hello world", "O"))  # Output: hell wrld