def count_chars(string: str, char: str) -> int:
    count_cycles = 0
    count_letters = 0
    while count_cycles < len(string):
        if string[count_cycles].lower() == char.lower():
            count_letters += 1
        count_cycles += 1
    return count_letters

print(count_chars("hello world", "o"))  # Output: 2