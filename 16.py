def is_contains_char(line: str, letter: str) -> bool:
    count_cycles = 0
    while count_cycles < len(line):
        if line[count_cycles] == letter:
            return True
        count_cycles += 1
    return False

print(is_contains_char("hello world", "W"))  # Output: True