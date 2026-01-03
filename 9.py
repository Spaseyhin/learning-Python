def get_type_of_sentence(sentence: str) -> str:
    last_char = sentence[-1]
    if last_char == '?':
        return 'question'
    return 'normal'


def get_type_of_sentence(sentence: str) -> str:
    last_char = sentence[-1]
    return 'question' if last_char == '?' else 'normal'