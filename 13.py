def add_spaces(text: str) -> str:
    result = ''
    i = 0
    while i < len(text):
        result = result + text[i]
        if i != len(text) - 1: 
            result += " "
        i = i + 1
    return result
    